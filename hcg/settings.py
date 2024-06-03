from pathlib import Path
import os
from .ckeditor_settings import CKEDITOR_5_CONFIGS

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9t52$h5v60v@^&)lx$)v!hq3j2#ox#$+_q&x(9phzz!b@53l(#'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'vacancies',
    'website',
    'posts',
]

THIRD_PARTY_APPS = [
    'django_ckeditor_5',
    'rest_framework',
    'django_filters',
]

INSTALLED_APPS = INSTALLED_APPS + MY_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hcg.urls'

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

WSGI_APPLICATION = 'hcg.wsgi.application'

CKEDITOR_5_CUSTOM_CSS = 'css/ckeditor5/admin_dark_mode_fix.css'

ROOT_URLCONF = 'hcg.urls'

STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',  
        'PORT': '5432',
    }
}

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

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 4,
    'DEFAULT_OFFSET': 0,
    'DEFAULT_LIMIT': 4,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'LIMIT_QUERY_PARAM': 'limit',
    'OFFSET_QUERY_PARAM': 'offset',
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'IN'

USE_I18N = True

USE_TZ = True

TIME_ZONE = 'UTC'

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = "/static/"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CKEDITOR_5_CUSTOM_CSS = 'css/ckeditor5/admin_dark_mode_fix.css'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587 
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'abhayrathi448@gmail.com'  
EMAIL_HOST_PASSWORD = 'cqtrwvhcsveujydi' 