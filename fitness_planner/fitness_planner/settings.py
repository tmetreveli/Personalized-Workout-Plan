# settings.py

import os
import environ

env = environ.Env()
# Reading .env file
environ.Env.read_env()



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'sixdf_*7jc)$e2)pl@6fpg#ak((oc#5#nplig6r*(tshwk%1jz'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DATABASE', 'fitness_planner'),
        'USER': os.environ.get('POSTGRES_USERNAME', 'postgres'),  
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'messi10'),  
        'HOST': os.environ.get('POSTGRES_REMOTE_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_REMOTE_PORT', '5432'),
        'OPTIONS': {'sslmode': 'disable'}

    }
}
DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular_sidecar',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'user',  
    'fitness_planner'
]
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # Other authentication classes if needed
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
# Whitenoise to serve static files.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SPECTACULAR_SETTINGS = {

    "TITLE": "Fitness Tracker",
    "VERSION": 'v1',
    "DESCRIPTION": "APIs to enable fitness tracking and enable workour plan creation",
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'SECURITY': [
        {
            'Bearer': []
        }
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Path were Django will look for static directory and CSS-Styling.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')  # Path for django to look static at.

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=100),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=100),
}

ROOT_URLCONF = 'fitness_planner.urls'
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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