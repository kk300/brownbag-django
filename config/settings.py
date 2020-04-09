"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zjs0_cv9rxsqx2b5&ahi=0!98*4i3w7d+yf3^5-s=pxo7r5+-9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'brownbags.apps.BrownbagsConfig',
    'accounts.apps.AccountsConfig',
]

if DEBUG:
    INSTALLED_APPS += [
        'django_extensions',
        #'debug_toolbar',
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

# for DEBUG
'''
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
'''

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'dist/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'contrib'),
)

STATICFILES_FINDERS = (
    # settings.STATICFILES_DIRSに設定したディレクトリからファイルを読み込む
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # アプリケーションのstaticディレクトリからファイルを読み込みむ
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'uploads')
MEDIA_URL = '/uploads/'

# accountsというアプリケーションです
# see also: DjangoでUserモデルのカスタマイズ <https://narito.ninja/blog/detail/39/>
AUTH_USER_MODEL = 'accounts.User'

# LOGGING
# ------------------------------------------------------------------------------

LOGGING_PATH = os.path.join(BASE_DIR, 'logs', 'uploads')
LOGGING_FILE = 'app.log'

if os.name == 'nt':
    LOGGING = {
        'version': 1,   # これを設定しないと怒られる
        'formatters': {
            'all': {
                'format': ':'.join([
                    "[%(levelname)s]",
                    "%(asctime)s",
                    "%(process)d",
                    "%(thread)d",
                    "%(message)s",
                ])
            },
        },
        'handlers': {
            'console': {  # 標準出力
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'all',
            },
        },
        'loggers': {
            'common': {  # commandという名前のloggerを定義
                'handlers': ['console'],
                'level': 'DEBUG',
            },
            'api': {  # detectionという名前のloggerを定義
                'handlers': ['console'],
                'level': 'DEBUG',
            }
        },
    }
else:
    LOGGING = {
        'version': 1,   # これを設定しないと怒られる
        'formatters': {
            'all': {
                'format': ':'.join([
                    "[%(levelname)s]",
                    "%(asctime)s",
                    "%(process)d",
                    "%(thread)d",
                    "%(message)s",
                ])
            },
        },
        'handlers': {
            'file_time_rotation': { # 時刻ローテート
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOGGING_PATH, LOGGING_FILE),
                'formatter': 'all',
                'when': 'D',
                'interval': 1,
                #'backupCount': 30,
            },
            'console': { # 標準出力
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'all',
            },
        },
        'loggers': {
            'common': {  # commandという名前のloggerを定義
                'handlers': ['file_time_rotation', 'console' ],
                'level': 'DEBUG',
            },
            'api': {  # detectionという名前のloggerを定義
                'handlers': ['file_time_rotation', 'console'],
                'level': 'DEBUG',
            },
        },
    }