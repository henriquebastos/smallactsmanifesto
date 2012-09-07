#coding: utf-8
import os
from os.path import abspath, basename, dirname, join, pardir
import subprocess


def adjust_options(options, args):
    BOOTSTRAP_PATH = abspath(dirname(__file__))

    # force a destdir
    while len(args):
        args.pop()

    args.append(join(BOOTSTRAP_PATH, pardir))


def extend_parser(parser):
    # override default options
    parser.set_defaults(no_site_packages=True,
                        unzip_setuptools=True,
                        use_distribute=True)

def after_install(options, home_dir):
    def run(cmd, *args):
        executable = join(home_dir, 'bin', cmd)
        command = [executable] + list(args)
        subprocess.call(command)

    # Install project requirements
    requirements = abspath(
        join(home_dir, 'requirements.txt')
    )
    run('pip', 'install', '-r', requirements)
