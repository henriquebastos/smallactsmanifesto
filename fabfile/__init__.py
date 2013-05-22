# coding: utf-8
from unipath import Path
from .helpers import Project

# Exposes other functionalities
import setup
import deploy
import db
import config
import django


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

