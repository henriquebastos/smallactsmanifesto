# coding: utf-8
from unipath import Path
from fabric.api import task, local, run, lcd, put, env
from .helpers import timestamp


@task
def push(revision):
    '''
    Push the code to the right place on the server.
    '''
    rev = local('git rev-parse %s' % revision, capture=True)
    local_archive = Path('/tmp/%s.tar.bz2' % rev)
    remote_archive = Path(env.PROJECT.tmp, local_archive.name)

    local('git archive --format=tar %s | bzip2 -c > %s' % (rev, local_archive))
    put(local_archive, remote_archive)

    release_dir = Path(env.PROJECT.releases, timestamp())
    run('mkdir -p %s' % release_dir)
    run('tar jxf %s -C %s' % (remote_archive, release_dir))

    return release_dir


def build():
    '''
    Build the pushed version installing packages, running migrations, etc.
    '''
    pass


def release():
    '''
    Release the current build activating it on the server.
    '''

def restart():
    '''
    Restart all services.
    '''


@task(default=True)
def deploy(revision):
    '''
    Make the application deploy.

    Example: fab production deploy:1.2
    '''
    require('settings')
    env.user = 'deploy'
    release_dir = _upload_source(revision)

    with cd(release_dir):
        run("sudo pip install -r host/requirements.txt")
        run("python manage.py syncdb --noinput --migrate --settings=%(settings)s" % env)
        run("python manage.py collectstatic --noinput --settings=%(settings)s" % env)

    with cd(env.PROJECT_RELEASES):
        run('rm -rf current')
        run('ln -s %s current' % release_dir)

    run('sudo /etc/init.d/nginx restart')
    run("sudo init Q")
    with settings(warn_only=True):
        run('sudo initctl stop wttd instance=%(settings)s' % env)
    run('sudo initctl start wttd instance=%(settings)s' % env)

    crontab_file = os.path.join(env.PROJECT_CURRENT, 'host/wttd.cron')
    run('sed -i "s|ENVIRONMENT|%s|g" %s' % (env.environment, crontab_file))
    run('sed -i "s|HOST|%s|g" %s' % (env.hosts[0], crontab_file))
    run('crontab %s' % crontab_file)
