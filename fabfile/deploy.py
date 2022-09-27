# coding: utf-8
from unipath import Path
from fabric.api import task, local, run, cd, put, env, prefix, require
from .helpers import timestamp


@task
def push(revision):
    """
    Push the code to the right place on the server.
    """
    rev = local(f'git rev-parse {revision}', capture=True)
    local_archive = Path(f'{rev}.tar.bz2')
    remote_archive = Path(env.PROJECT.tmp, local_archive.name)

    local(f'git archive --format=tar {rev} | bzip2 -c > {local_archive}')
    put(local_archive, remote_archive)

    release_dir = Path(env.PROJECT.releases, timestamp())
    run(f'mkdir -p {release_dir}')
    run(f'tar jxf {remote_archive} -C {release_dir}')

    # cleanup
    local(f'rm {local_archive}')

    return release_dir


@task
def build(release_dir):
    """
    Build the pushed version installing packages, running migrations, etc.
    """
    with cd(release_dir):
        release_static = Path(release_dir, env.PROJECT.package, 'static')
        release_media = Path(release_dir, env.PROJECT.package, 'media')
        release_settings = Path(release_dir, env.PROJECT.package, 'settings.ini')

        run(f'ln -s {env.PROJECT.settings} {release_settings}')
        run("python bootstrap")

        with prefix('source bin/activate'):
            run("python manage.py syncdb --noinput --migrate --settings=%(settings)s" % env)
            run("python manage.py collectstatic --noinput --settings=%(settings)s" % env)

        run('mkdir -p public')
        run(f'ln -s {release_static} public/')
        run(f'ln -s {env.PROJECT.media} public/')
        run(f'ln -s {env.PROJECT.media} {release_media}')


@task
def release(release_dir):
    """
    Release the current build activating it on the server.
    """
    with cd(env.PROJECT.releases):
        run('rm -rf current')
        run(f'ln -s {release_dir} current')


@task
def restart():
    """
    Restart all services.
    """
    run('pkill python')
    run('touch %(current)s/passenger_wsgi.py' % env.PROJECT)


@task(default=True)
def deploy(revision):
    """
    Make the application deploy.

    Example: fab production deploy:1.2
    """
    require('PROJECT', provided_by=['stage', 'production'])

    release_dir = push(revision)
    build(release_dir)
    release(release_dir)
    restart()
