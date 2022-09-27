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

    remote_file = f'{env.PROJECT.tmp}/{env.host}-{timestamp()}.json.bz2'

    with cd(env.PROJECT.current):
        with prefix('source bin/activate'):
            run(
                f'python manage.py dumpdata {apps_or_models} --indent 4 | bzip2 -c  > {remote_file}'
            )

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
            run(f'bunzip2 {remote_file}')
            remote_file = remote_file.replace('.bz2', '')

        with prefix('source bin/activate'):
            run(f'python manage.py loaddata {remote_file}')

    run(f'rm {remote_file}')
