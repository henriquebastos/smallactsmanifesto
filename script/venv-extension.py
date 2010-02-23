from os.path import abspath, dirname, join
import subprocess


def extend_parser(parser):
    # overide default options
    parser.set_default('no_site_packages', True)
    parser.set_default('unzip_setuptools', True)
    parser.set_default('use_distribute', True)

    # where is the source code?
    default_project_src = abspath(join(dirname(__file__), '..'))
    print default_project_src
    parser.add_option("-s", "--source", dest="project_src", metavar="SRC", 
        default=default_project_src, help="Path to the source directory.")


def after_install(options, home_dir):
    def run(cmd, *args):
        executable = join(home_dir, 'bin', cmd)
        command = [executable] + list(args)
        subprocess.call(command)
    
    # list of required packages
    requirements = (
        'ipython',
        'django',
    )

    # install packages
    for package in requirements:
        run('pip', 'install', package)
