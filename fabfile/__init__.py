# coding: utf-8
from fabric.api import env, task, settings, hide, cd, run, prefix
from unipath import Path
from .helpers import timestamp, Project

import setup
import deploy
import db
import config


# Always run fabric from the repository root dir.
Path(__file__).parent.parent.chdir()


@task
def stage():
    env.user = 'smallactsmanifesto'
    env.hosts = ['stage.smallactsmanifesto.org']
    env.settings = 'smallactsmanifesto.settings'
    env.PROJECT = Project('~', env.hosts[0], env.user)


@task
def manage(command):
    assert command
    with settings(hide('warnings'), warn_only=True):
        with cd(env.PROJECT.current):
            with prefix('source bin/activate'):
                run('python manage.py %s' % command)
