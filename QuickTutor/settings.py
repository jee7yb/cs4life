"""
Django settings for QuickTutor project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import dotenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This is new:
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0=+%_)z8*!16i@e(v!1kome^xrly#-d4b#(hz@(qxkx7sc+0k!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cs4life-quicktutor.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'main.apps.MainConfig',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount',
    'allauth.account',
    'allauth',
    'multiselectfield',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'QuickTutor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'QuickTutor.wsgi.application'

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''

DATABASES = {'default': dj_database_url.parse('postgres://postgres:Keshav00@localhost:5432/quicktutor')}
# DATABASES = {}
# DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# DATABASES = {
#     'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'quickTutor',
#         'USER': 'kailaney',
#         'PASSWORD': 'Keshav00',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# if 'HEROKU' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': 'd6humjm2sv80ba',
#             'USER': 'bonxsspvtuuons',
#             'PASSWORD': '2c88c692268646249453ec7448aed5dbc5c3ce859738794d5a9e86abd004fd1d',
#             'HOST': 'ec2-3-234-169-147.compute-1.amazonaws.com',
#             'PORT': '5432',
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': 'quicktutor4',
#             'USER': 'groupuser',
#             'PASSWORD': 'tutoring!',
#             'HOST': '127.0.0.1',
#             'PORT': '5432',
#         }
#     }



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

SITE_ID = 1

LOGIN_REDIRECT_URL = "/loggedIn"


#AUTH_USER_MODEL = 'main.CustomUser'

# Activate Django-Heroku.
# django_heroku.settings(locals())
if 'HEROKU' in os.environ:
    import django_heroku
    django_heroku.settings(locals())

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'VERIFIED_EMAIL': True,
    }
}
