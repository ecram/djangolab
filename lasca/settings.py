import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = ''

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost','127.0.0.1','*']

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'academic',
    'publications',
    'mod_wsgi.server',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'root.urls'

WSGI_APPLICATION = 'root.wsgi.application'

ADMINS = (('admin', 'admin@django.lab'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangolab_db',
        'USER': 'postgres',
        'PASSWORD': 'your_pass',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
        '/var/www/src/static/templates'
    )

GEOIP_PATH = '/var/www/src/static/geoip'

#if DEBUG:
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/www/src/static/'
MEDIA_ROOT = '/var/www/src/media/'
STATICFILES_DIRS = (
            '/var/www/src/static/static/',
        )

#Captcha methods:
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_LETTER_ROTATION =  (-10,10)
CAPTCHA_FONT_SIZE = 30

# Send email config
EMAIL_PORT = 25
EMAIL_HOST = 'smtp.your_dominio'
DEFAULT_FROM_EMAIL = 'admin@django.lab'

THUMBNAIL_DEBUG = True

SITE_ID = 1
