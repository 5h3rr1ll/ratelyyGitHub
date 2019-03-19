"""
Django settings for ratelyyDjango project.

Generated by 'django-admin startproject' using Django 1.11.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f81ef2_sh7+)vg+&#nrxjo%@xa1mbep#mofsnvcob&9$uu9jb4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ratelyyDjangoEnv.p5j68a2z24.eu-central-1.elasticbeanstalk.com',"127.0.0.1","localhost"]


# Application definition

INSTALLED_APPS = [
    'mvpLogoGrab',
    "accounts",
    "mvpScanWebApp",
    'ratelyyDatabase',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "ratelyyDjango.middleware.LoginRequireMiddleware",
]

ROOT_URLCONF = 'ratelyyDjango.urls'

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

WSGI_APPLICATION = 'ratelyyDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
   # ‘sqlite3’: {
   #     ‘ENGINE’: ‘django.db.backends.sqlite3’,
   #     ‘NAME’: os.path.join(BASE_DIR, ‘db.sqlite3’),
   # },

   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'USER': 'd025764e',
       'NAME': 'd025764e',
       'PASSWORD': 'r4tl3yy',
       'HOST': '85.13.154.99',
       'PORT': '3306',
       'OPTIONS': {
           'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
           }
   },
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

LOGIN_URL = "/accounts/login"
LOGIN_REDIRECT_URL = "/accounts/profile"
LOGIN_EXEMPT_URLS = (
    r"^accounts/logout/$",
    r"^accounts/register/$",
    r"^accounts/reset-password/$",
)

# TODO: Need to set up a propper email server here
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
