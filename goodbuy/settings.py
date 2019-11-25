"""
Django settings for Goodbuy project.

Generated by 'django-admin startproject' using Django 1.11.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG_VALUE") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# Application definition
INSTALLED_APPS = [
    "home.apps.HomeConfig",
    "accounts.apps.AccountsConfig",
    "codeScanner.apps.CodeScannerConfig",
    "goodbuyDatabase.apps.GoodbuyDatabaseConfig",
    "scraper",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "crispy_forms",
    "storages",
    "corsheaders",
]


CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # TODO: Not sure if this middleware is really helpful, things like
    # /?next=/ -functionality <-- is missing then
    # "goodbuy.middleware.LoginRequireMiddleware",
]

CORS_ORIGIN_WHITELIST = [
    "https://goodbuy.netlify.com",
    "https://goodbuy-dev.netlify.com/",
]

ROOT_URLCONF = "goodbuy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "goodbuy.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "goodbuy/staticfiles")
STATIC_URL = "/static/"

# Here you define where Django shoul save uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, "goodbuy/media")
# define how Django serve the files back, means: what to type in to the URL
MEDIA_URL = "/media/"

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "home"

LOGIN_EXEMPT_URLS = (
    r"^accounts/logout/$",
    r"^accounts/register/$",
    r"^accounts/reset-password/$",
    r"^accounts/password_reset_done/$",
    r"^accounts/reset-password/confirm/(<uidb64>[0-9A-Za-z]+)-(<token>.+)/$",
    r"^accounts/reset-password/complete/$",
)

# TODO: make sure every email adresse can reset password, atm only gmail can
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# Activate Django-Heroku.
django_heroku.settings(locals())

# Get's the values from the system environment
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

# Same diles don't overwrite eachother
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
# This setting prevented adding access infomrations to the file urls
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
