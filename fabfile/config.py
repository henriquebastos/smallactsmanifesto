# coding: utf-8
from unipath import Path
from fabric.api import task, run, env, require, settings, hide, fastprint, get, put
from fabric.contrib.files import append, sed


@task(default=True)
def list():
    """
    List remote configurations.
    """
    require('PROJECT', provided_by=['stage', 'production'])

    fastprint(run('cat %(settings)s' % env.PROJECT, quiet=True))


@task
def set(option, value):
    """
    Update or create option line from remote settings.ini
    """
    option = option.lower()

    before = f'{option} = .*'
    after = f'{option} = {value}'

    if contains(env.PROJECT.settings, before):
        sed(env.PROJECT.settings, before, after, backup='')
    else:
        append(env.PROJECT.settings, after)

    # sanity check
    assert contains(env.PROJECT.settings, after), 'Config not found: "%s"' % after


@task
def remove(option):
    """
    Remove option line from remote settings.ini
    """
    option = option.lower()

    before = f'{option} = .*'
    if contains(env.PROJECT.settings, before):
        after = ''

        sed(env.PROJECT.settings, before, after, backup='')

    # sanity check
    assert not contains(env.PROJECT.settings, f'{option}.*'), (
        'Config found: "%s"' % option
    )


@task
def download():
    """
    Download remote settings.ini.
    """
    get(env.PROJECT.settings, Path(env.lcwd, Path(env.PROJECT.settings).name))


@task
def upload(config_file):
    """
    Upload a config file to replace remote settings.ini.
    """
    put(config_file, env.PROJECT.settings)


def contains(filename, text):
    with settings(hide('everything'), warn_only=True):
        cmd = 'egrep "^%s$" %s' % (text, filename)
        return run(cmd).succeeded
