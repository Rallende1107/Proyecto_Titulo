"""
Django settings for projectoWeb project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.getenv("DEBUG")


HOSTS_BASE = ['0.0.0.0', 'proyectotitulo-production-1f3a.up.railway.app', 'vecina-hay-pan.cl', 'proyectotitulo-dev.up.railway.app','*']

ALLOWED_HOSTS = HOSTS_BASE


# Application definition

BASE_APP =[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APP = [
    'rest_framework',
    'simple_history',
    'rest_framework.authtoken',
    'corsheaders',
    'whitenoise.runserver_nostatic',
]

LOCAL_APP = [
'apps.haypan',
]


INSTALLED_APPS = BASE_APP + EXTERNAL_APP + LOCAL_APP

TOKEN_EXPIRED_AFTER_SECONDS = 86400
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.common.CommonMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'projectoWeb.urls'

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
                'apps.haypan.context_processor.total_carrito',
            ],
        },
    },
]
WSGI_APPLICATION = 'projectoWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



# ENTORNO = 'DEV'
ENTORNO = 'PROD'


if ENTORNO == 'PROD':
    DATABASES = {
        'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))

    }
elif ENTORNO == 'DEV':
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-CL'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
STATIC_ROOT = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'haypan.Usuario'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

LOGIN_URL = '/login/'
# LOGOUT_REDIRECT_URL = '//'
APPEND_SLASH = False

CORS_ALLOWED_ORIGINS = ['https://vecina-hay-pan.cl','https://*']
# "http://localhost:8100"
CORS_ORIGIN_WHITELIST = ['https://vecina-hay-pan.cl','https://*']
# "http://localhost:8100"

CSRF_TRUSTED_ORIGINS = ['https://proyectotitulo-production-1f3a.up.railway.app', 'https://proyectotitulo-dev.up.railway.app', 'https://vecina-hay-pan.cl','https://*']
# 'http://localhost', 'http://127.0.0.1',


