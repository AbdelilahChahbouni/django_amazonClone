
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rs(7rxl8-5v1abr2j^fi@+i2%v@nk-)ta($8#8+!bm8ua)x51+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'debug_toolbar',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    'rosetta',
    'product',
    'settings',
    'orders',
    'drf_yasg',
    'bootstrap5'

    
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


LOCALE_PATHS = (
    'locale',
)

LANGUAGES = [
    ('ar', ('Arabic')),
    ('en', ('English')),
]


ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.company_context_processor.get_company_info',
                'orders.cart_context_processor.get_or_create_cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.postgresql',
       # 'NAME':'mydb',
       # 'USER': 'postgres',
       # 'PASSWORD':'postgres',
       # 'HOST': 'db',
       # 'PORT': '5432',
   # }
#}






# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static/",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
       'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30
}

#CACHES = {
    #"default": {
       # "BACKEND": "django.core.cache.backends.redis.RedisCache",
       # "LOCATION": 'redis://redis:6379/0',
    #}
#}

# the redis run from localhost 
#CELERY_BROKER_URL = 'redis://localhost:6379/0'
#CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# the redis run from doker image
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'


# login with email

AUTHENTICATION_BACKENDS = ['accounts.backends.EmailOrUsernameModelBackend']
LOGIN_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "dev4testemail@gmail.com"
EMAIL_HOST_PASSWORD = "yxmggrrtjnkrdzmb"
