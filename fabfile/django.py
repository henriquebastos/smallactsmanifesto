# coding: utf-8
from fabric.api import env, task, settings, hide, cd, run, prefix


@task
def manage(command):
    assert command
    with settings(hide('warnings'), warn_only=True):
        with cd(env.PROJECT.current):
            with prefix('source bin/activate'):
                run('python manage.py %s' % command)
