# coding: utf-8
from datetime import datetime
from fabric.api import env


class Project(dict):
    """
    Describes the remote directory structure for a project.
    """
    def __init__(self, rootdir, appname, package):
        appdir = f'{rootdir}/{appname}'

        super(Project, self).__init__(
            appdir=appdir,
            releases=f'{appdir}/releases',
            current=f'{appdir}/releases/current',
            share=f'{appdir}/share',
            media=f'{appdir}/share/media',
            settings=f'{appdir}/share/settings.ini',
            tmp=f'{appdir}/tmp',
            logs=f'{rootdir}/logs/{appname}',
            package=package,
        )

    def __getattr__(self, item):
        if item in self:
            return self[item]

        raise AttributeError("'%s' object has no attribute '%s'" % (
            self.__name__, item))


def timestamp():
    return datetime.now().strftime("%Y-%m-%d-%Hh%Mm%Ss")


def make_environment(name, domain):
    """
    Configure Fabric's environment according our conventions.
    """
    project = domain.partition('.')[0]
    cname = f'{name}.{domain}'
    env.user = project
    env.hosts = [cname]
    env.settings = f'{project}.settings'
    env.PROJECT = Project('~', cname, project)
