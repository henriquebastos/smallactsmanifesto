# coding: utf-8
import os
import sys

PROJECT_ROOT = os.path.dirname(__file__)

this_file = os.path.join(PROJECT_ROOT, 'bin', 'activate_this.py')
execfile(this_file, dict(__file__=this_file))

#INTERP = os.path.join(PROJECT_ROOT, 'bin', 'python')
#INTERP is present twice so that the new python interpreter knows the actual executable path
#if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, PROJECT_ROOT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'smallactsmanifesto.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
