from pathlib import Path
import os
from .ckeditor_settings import CKEDITOR_5_CONFIGS


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'fk(#5!d*g1=nk7&8)aj5lo0cdp08nlml89*8epgptp3ucdpd9y'

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
    'storages',
    #'whitenoise.runserver_nostatic',
    #'django-celery-results',
    'rest_framework_swagger',
    'drf_spectacular',
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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'HCG APIs',
    'DESCRIPTION': 'Backend of HCG',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
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

GDAL_LIBRARY_PATH = '/opt/homebrew/opt/gdal/lib/libgdal.dylib'
GEOS_LIBRARY_PATH = '/opt/homebrew/opt/geos/lib/libgeos_c.dylib'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'abhayrathi448@gmail.com'
EMAIL_HOST_PASSWORD = 'cqtrwvhcsveujydi'
DEFAULT_FROM_EMAIL = 'abhayrathi448@gmail.com'

# Uncomment and update these settings if you use AWS S3 for storage
# AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
# AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
# AWS_S3_FILE_OVERWRITE = env.bool('AWS_S3_FILE_OVERWRITE')
# AWS_DEFAULT_ACL = env('AWS_DEFAULT_ACL')
# AWS_S3_VERIFY = env.bool('AWS_S3_VERIFY')
# STATICFILES_STORAGE = env('STATICFILES_STORAGE')
# DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = {'application/json'}
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Paris'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_BROKER_URL = 'redis://localhost:6379/9'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/9'