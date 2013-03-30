# coding: utf-8
from dj_database_url import parse as db_url
from unipath import Path
from smallactsmanifesto.config import DjangoConfig

PROJECT_ROOT = Path(__file__).parent

config = DjangoConfig(PROJECT_ROOT.child('settings.ini'))

DEBUG = config('DEBUG', default=False, type=bool)
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': config('DATABASE_URL', default='sqlite:///' + PROJECT_ROOT.child('database.db'), type=db_url)
}

SITE_ID = 1

TIME_ZONE = 'America/Sao_Paulo'
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = PROJECT_ROOT.child('media')
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_ROOT.child('static')
STATIC_URL = '/static/'

SECRET_KEY = config('SECRET_KEY')

ROOT_URLCONF = 'smallactsmanifesto.urls'

WSGI_APPLICATION = 'smallactsmanifesto.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'smallactsmanifesto.core',
    'smallactsmanifesto.signatures',
)

ADMINS = (
    ('Small Acts Manifesto', 'admin@smallactsmanifesto.org'),
)

DEFAULT_FROM_EMAIL = 'admin@smallactsmanifesto.org'

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, type=int)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, type=bool)
