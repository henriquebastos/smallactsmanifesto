# coding: utf-8
import os
import sys


PROJECT_ROOT = os.path.dirname(__file__)

sys.path.insert(0, PROJECT_ROOT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'smallactsmanifesto.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
