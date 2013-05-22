# coding: utf-8
from fabric.api import task
from unipath import Path
from .helpers import make_environment

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
    make_environment('stage', 'smallactsmanifesto.org')


@task
def production():
    make_environment('production', 'smallactsmanifesto.org')
