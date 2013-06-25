# coding: utf-8
from unipath import Path
from fabric.api import task
from fabric_dreamhost import (
    make_environment,
    # Tasks:
    setup,
    deploy,
    db,
    config,
    django
)


# Always run fabric from the repository root dir.
Path(__file__).parent.parent.chdir()


@task
def stage():
    make_environment('stage', 'smallactsmanifesto.org')


@task
def production():
    make_environment('production', 'smallactsmanifesto.org')
