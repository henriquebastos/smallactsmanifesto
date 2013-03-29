# coding: utf-8
from fabric.api import env, run, require, abort, task
from fabric.colors import red, yellow
from fabric.contrib.console import confirm
from fabric.contrib.files import exists


@task
def server():
    print """
    Dreamhost Setup

    Consider that we're trying to setup a *fully hosted* domain
    "myproject.com.br".

    0.  Login to you Dreamhost Panel
    1.  On the "Main Menu", go to "Domains", then to "Manage Domains"
        and click on "Add New Domain / Sub-Domain".
    2.  Find the section "Domain name".
    3.  Set "Domain to host" to your domain name: myproject.com.br
    4.  On "Do you want the www in your URL?" choose the last option,
        "Remove WWW..."
    5.  Find the section "Users, Files, and Paths".
    6.  on "Run this domain under user" select the option "Create a new
        user" and define the user as: myproject
    7.  Set "Web directory" to: myproject.com.br/releases/current/public
    8.  Find the section "Web options";
    9.  Check the option "Passenger (Ruby/Python apps only)"
    10. Click on the "Fully host this domain" button to save.
    11. On the "Main Menu", go to "Users", then to "Manage Users".
    12. Find the new user named "myproject" and click the "Edit" button.
    13. Change the option "User Account Type" to "Shell account".
    14. Define a password typing to "New Password" and "New Password
        Again".
    15. Click the "Save Changes" button.
    """


@task
def application():
    """
    Setup application directories: fab stage setup.application

    At Dreamhost we have 1 user for 1 app with N environments.
    This makes easy to give deploy access to different ssh keys.

    The project directory layout is:

      ~/user (rootdir)
      +---- /stage.myproject.com.br (appdir)
      |     +---- /releases
      |     |     +---- /current
      |     +---- /share
      +---- /logs
            +---- /stage.myproject.com.br (logs)
    """
    require('PROJECT', provided_by=['stage', 'production'])

    if exists(env.PROJECT.appdir):
        print(yellow('Application detected at: %(appdir)s' % env.PROJECT))
        if confirm(red('Rebuild application?'), default=False):
            run('rm -rf %(appdir)s' % env.PROJECT)
        else:
            abort('Application already exists.')

    # Create directory structure
    run('mkdir -m 755 -p %(appdir)s' % env.PROJECT)
    run('mkdir -m 755 -p %(releases)s' % env.PROJECT)
    run('mkdir -m 755 -p %(current)s' % env.PROJECT)
    run('mkdir -m 755 -p %(share)s' % env.PROJECT)
    run('mkdir -m 755 -p %(media)s' % env.PROJECT)
    run('mkdir -m 755 -p %(tmp)s' % env.PROJECT)
    run('mkdir -m 755 -p %(logs)s' % env.PROJECT)

    # Initialize environment settings file
    run('echo "[settings]\n" >> %(settings)s' % env.PROJECT)
    run('chmod 600 %(settings)s' % env.PROJECT)


@task
def delete_app():
    """
    Delete an application instance.
    """
    require('PROJECT', provided_by=['stage', 'production'])

    question = red('Do you want to DELETE the app at %(appdir)s ?' % env.PROJECT)

    if exists(env.PROJECT.appdir) and confirm(question, default=False):
        run('rm -rf %(appdir)s' % env.PROJECT)
