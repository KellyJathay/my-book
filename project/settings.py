"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from decouple import config
from dj_database_url import parse as db_url
from django.contrib.messages import constants as messages

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


# Application definition

INSTALLED_APPS = [
    'audiobooks.apps.AudiobooksConfig',
    'constance',
    'constance.backends.database',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'rest_framework',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'constance.context_processors.config',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default=f'sqlite:///{BASE_DIR}/db.sqlite3',
        cast=db_url
    )
}


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', cast=str, default='en-us')

TIME_ZONE = config('TIME_ZONE', cast=str, default='UTC')

USE_I18N = config('USE_I18N', cast=bool, default=True)

USE_L10N = config('USE_L10N', cast=bool, default=True)

USE_TZ = config('USE_TZ', cast=bool, default=True)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = config('STATIC_ROOT', cast=str, default='static_prd/')
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join('static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'ELEMENTS_PER_PAGE': (10, 'Quantidade de itens exibidos por página (Usuários, audiobooks, etc).', int),
    'SYSTEM_NAME': ('IN VOICE', 'O nome do sistema mostrado no canto superior esquerdo', str),
    'TIME_TO_EXPIRE_SESSION': (31556952, 'Tempo em segundos para expirar sessão (Padrão 1 ano)', int),
}

MESSAGE_TAGS = {
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

LOGIN_URL = '/sign_in/'
LOGOUT_REDIRECT_URL = '/sign_out/'

DEFAULT_ADMINISTRATOR_USERNAME = config('DEFAULT_ADMINISTRATOR_USERNAME', cast=str, default='admin')
DEFAULT_ADMINISTRATOR_PASSWORD = config('DEFAULT_ADMINISTRATOR_PASSWORD', cast=str, default='12345')
DEFAULT_ADMINISTRATOR_EMAIL = config('DEFAULT_ADMINISTRATOR_PASSWORD', cast=str, default='admin@admin.com')

DEFAULT_MEDIA_ROOT = f'{BASE_DIR}/media'
MEDIA_ROOT = config('MEDIA_ROOT', cast=str, default=DEFAULT_MEDIA_ROOT)
MEDIA_URL = config('MEDIA_URL', cast=str, default='/media/')

FRONT_COVER_DIRECTORY_PATH = f'{MEDIA_ROOT}/front_convers'
RECORDING_FILE_DIRECTORY_PATH = f'{MEDIA_ROOT}/audiobooks'

MEDIA_PATHS = [MEDIA_ROOT, FRONT_COVER_DIRECTORY_PATH, RECORDING_FILE_DIRECTORY_PATH,]

for path in MEDIA_PATHS:
    if not os.path.exists(path):
        os.mkdir(path)