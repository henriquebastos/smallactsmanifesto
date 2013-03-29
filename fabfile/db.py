# coding: utf-8
import os
from fabric.api import task, get, env, put, abort, run, cd, require, prefix
from unipath import Path
from .helpers import timestamp


@task
def dumpdata(apps_or_models=''):
    '''
    Connect to Dreamhost server, generate a database dump and
    download it.

    Usage: fab stage db.dump
    '''
    require('PROJECT', provided_by=['stage', 'production'])

    remote_file = '%s/%s-%s.json.bz2' % (env.PROJECT.tmp, env.host, timestamp())

    with cd(env.PROJECT.current):
        with prefix('source bin/activate'):
            run('python manage.py dumpdata %s --indent 4 | bzip2 -c  > %s' % (apps_or_models, remote_file))
            get(remote_file, os.getcwd())


@task
def loaddata(local_file):
    '''
    Connect to Dreamhost server, upload a local database dump and
    restore it.

    Usage: fab stage db.restore:dumpfile.bz2
    '''
    require('PROJECT', provided_by=['stage', 'production'])

    local_file = Path(local_file)
    remote_file = Path(env.PROJECT.tmp, local_file.name)

    if put(local_file, remote_file).failed:
        abort('Failed to upload "%s"' % local_file)

    with cd(env.PROJECT.current):
        if '.bz2' in remote_file:
            run('bunzip2 %s' % remote_file)
            remote_file = remote_file.replace('.bz2', '')

        with prefix('source bin/activate'):
            run('python manage.py loaddata %s' % remote_file)

    run('rm %s' % remote_file)
