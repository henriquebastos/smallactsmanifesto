# coding: utf-8
from fabric.api import env, task, settings, hide, cd, run, prefix
from unipath import Path
from .helpers import Project

import setup
import deploy
import db
import config


# Always run fabric from the repository root dir.
Path(__file__).parent.parent.chdir()


@task
def stage():
    project = 'smallactsmanifesto'
    cname = 'stage.smallactsmanifesto.org'
    env.user = project
    env.hosts = [cname]
    env.settings = '%s.settings' % project
    env.PROJECT = Project('~', cname, project)


@task
def production():
    project = 'smallactsmanifesto'
    cname = 'production.smallactsmanifesto.org'
    env.user = project
    env.hosts = [cname]
    env.settings = '%s.settings' % project
    env.PROJECT = Project('~', cname, project)


@task
def manage(command):
    assert command
    with settings(hide('warnings'), warn_only=True):
        with cd(env.PROJECT.current):
            with prefix('source bin/activate'):
                run('python manage.py %s' % command)
