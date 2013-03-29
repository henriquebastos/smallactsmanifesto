# coding: utf-8
from fabric.api import env, task, settings, hide, cd, run
from unipath import Path
from .helpers import timestamp, Project

import setup
import deploy
import db


# Always run fabric from the repository root dir.
Path(__file__).parent.parent.chdir()

'''
production

deploy
db.dump - manage.py dumpdata | tar.gz -> download
db.restore - arquivo (tar.gz, json, sql, yaml) -> upload -> flush e loaddata
'''

@task
def stage():
    env.user = 'smallactsmanifesto'
    env.hosts = ['stage.smallactsmanifesto.org']
    env.settings = 'smallactsmanifesto.settings'
    env.PROJECT = Project('~', env.hosts[0])


def manage(command):
    assert command
    with settings(hide('warnings'), user='deploy', warn_only=True):
        with cd(env.PROJECT_CURRENT):
            run('python manage.py %s --settings=%s' % (command, env.settings))
