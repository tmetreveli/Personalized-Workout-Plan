# settings.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'sixdf_*7jc)$e2)pl@6fpg#ak((oc#5#nplig6r*(tshwk%1jz'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DATABASE', 'fitness_planner'),
        'USER': os.environ.get('POSTGRES_USERNAME','postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD','messi10'),
        'HOST': os.environ.get('POSTGRES_REMOTE_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_REMOTE_PORT','5432'),
        'OPTIONS': {'sslmode': 'disable'}
    }
}
DEBUG = True

ALLOWED_HOSTS = []

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }

}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'rest_framework_simplejwt',
    'user',  # Add your app name here,
    'fitness_planner'
]
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=100),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=100),
}

ROOT_URLCONF = 'fitness_planner.urls'
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
]

# Path were Django will look for static directory and CSS-Styling.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')  # Path for django to look static at.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        }
    },
]

# Other configurations...
