# coding: utf-8
from itertools import chain
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
LANGUAGES = (
    ('en', u'English'),
    ('es', u'Español'),
    ('pt-br', u'Português'),
)
LOCALE_PATHS = (
    PROJECT_ROOT.child('locale'),
)


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
    'django_nose',
    'captcha',
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


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


if config('CACHE_ENABLED', False, bool):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': PROJECT_ROOT.child('cache'),
            'TIMEOUT': 60 * 5,
            }
    }

    MIDDLEWARE_CLASSES = tuple(chain(
        (
            'django.middleware.cache.UpdateCacheMiddleware',
        ),
        MIDDLEWARE_CLASSES,
        (
            'django.middleware.http.ConditionalGetMiddleware',
            'django.middleware.gzip.GZipMiddleware',
            'django.middleware.cache.FetchFromCacheMiddleware',
        ),
    ))

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_USE_SSL = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--match=^(must|ensure|should|test|it_should)',
    '--where=%s' % PROJECT_ROOT,
    '--id-file=%s' % PROJECT_ROOT.child('.noseids'),
    '--all-modules',
    '--with-id',
    '--verbosity=1',
    '--nologcapture',
    '--rednose',
    ]

