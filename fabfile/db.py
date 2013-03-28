# coding: utf-8
from fabric.api import task, get, env, put, abort
from unittest import Path


@task
def dump():
    '''
    Connect to Dreamhost server, generate a database dump and
    download it.

    Usage: fab stage db.dump
    '''
    require('PROJECT', provided_by=['stage', 'production'])

    dumpfile = '%s/%s-%s.sql.bz2' % (env.PROJECT.tmp, env.host, timestamp())

    with cd(env.PROJECT.current):
        run('python manage.py dumpdata --all --indent 4 | bzip2 -c  > %(dumpfile)s' % dumpfile)
        get(dumpfile, os.getcwd())


@task
def restore(dumpfile):
    '''
    Connect to Dreamhost server, upload a local database dump and
    restore it.

    Usage: fab stage db.restore:dumpfile.bz2
    '''
    require('PROJECT', provided_by=['stage', 'production'])

    remote_file = put(Path(dumpfile), env.PROJECT.tmp)

    if remote_file.failed:
        abort('Failed to upload "%s"' % local_file)

    remote_file = Path(remote_file.pop())
    run()
