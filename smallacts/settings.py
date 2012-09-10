# Django settings for smallacts project.
from unipath import Path

PROJECT_ROOT = Path(__file__).parent

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Small Acts Manifesto', 'admin@smallactsmanifesto.org'),
)

DEFAULT_FROM_EMAIL = 'admin@smallactsmanifesto.org'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT.child('database.db'),
    }
}

SITE_ID = 1

TIME_ZONE = 'America/Sao_Paulo'
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = PROJECT_ROOT.child('media')
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_ROOT.child('static')
STATIC_URL = '/static/'

SECRET_KEY = '4&7-+%-5xeha_awet(s3**b!6+-29k*qq=r@xi!=@#v@f9^l6i'

ROOT_URLCONF = 'smallacts.urls'

WSGI_APPLICATION = 'smallacts.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'smallacts.core',
    'smallacts.signatures',
)
