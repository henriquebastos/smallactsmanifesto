# coding: utf-8
from datetime import datetime
from fabric.api import env


class Project(dict):
    """
    Describes the remote directory structure for a project.
    """
    def __init__(self, rootdir, appname, package):
        appdir = '%s/%s' % (rootdir, appname)

        super(Project, self).__init__(
            appdir   = appdir,
            releases = '%s/releases' % appdir,
            current  = '%s/releases/current' % appdir,
            share    = '%s/share' % appdir,
            media    = '%s/share/media' % appdir,
            settings = '%s/share/settings.ini' % appdir,
            tmp      = '%s/tmp' % appdir,
            logs     = '%s/logs/%s' % (rootdir, appname),

            package  = package,
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
    cname = '%s.%s' % (name, domain)
    env.user = project
    env.hosts = [cname]
    env.settings = '%s.settings' % project
    env.PROJECT = Project('~', cname, project)
