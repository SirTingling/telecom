"""
Django settings for the 'telegram' project.

For detailed settings documentation, refer to:
- Main settings: https://docs.djangoproject.com/en/3.0/topics/settings/
- Settings reference: https://docs.djangoproject.com/en/3.0/ref/settings/
- Deployment checklist: https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------- >>
import os # Import the os module for interacting with the operating system
from django.core.management.utils import get_random_secret_key # Import the get_random_secret_key function from the Django management utilities module
from django.contrib.messages import constants as messages # Import the constants module from the Django messages module


# ------- CORE SETTINGS -------
# Determine the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Ensure the safety of the application by using a secret key
SECRET_KEY = get_random_secret_key() # This is the secret key for the Django project
DEBUG = True  # Toggle debug mode (use 'False' in a production environment)
ALLOWED_HOSTS = []  # List of valid hosts for the application
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Primary configuration for URL routing
ROOT_URLCONF = 'application.urls' # This is the URL configuration module for the project
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Configuration for ASGI and WSGI applications
ASGI_APPLICATION = 'application.application-asgi.application' # This is the ASGI application configuration module for the project
WSGI_APPLICATION = 'application.application-wsgi.application' # This is the WSGI application configuration module for the project
# -------------------------------------------------------------------------------------------------------------------------------------------------

# ------- DATABASE SETTINGS -------
# Configuration for SQLite3 database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# -------------------------------------------------------------------------------------------------------------------------------------------------

# ------- INTERNATIONALIZATION SETTINGS -------
# Settings for language and time zone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# -------------------------------------------------------------------------------------------------------------------------------------------------

# ------- STATIC AND MEDIA SETTINGS -------
# Define URLs and directories for static and media files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# -------------------------------------------------------------------------------------------------------------------------------------------------

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# ------- INSTALLED APPS -------
# List of applications that are active within this Django project
INSTALLED_APPS = [
    'bootstrap4',
    'channels',
    'rest_framework',
    'posts',
    'chatroom',
    'memberProfiles',
    'requests',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# -------------------------------------------------------------------------------------------------------------------------------------------------

# ------- MIDDLEWARE SETTINGS -------
# List of middleware classes activated in the project
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # This middleware class is used to ensure that the application is secure
    'django.contrib.sessions.middleware.SessionMiddleware', # This middleware class is used to manage sessions
    'django.middleware.common.CommonMiddleware', # This middleware class is used to manage cookies
    'django.middleware.csrf.CsrfViewMiddleware', # This middleware class is used to manage cross-site request forgery
    'django.contrib.auth.middleware.AuthenticationMiddleware', # This middleware class is used to manage user authentication
    'django.contrib.messages.middleware.MessageMiddleware', # This middleware class is used to manage messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # This middleware class is used to manage clickjacking
]
# -------------------------------------------------------------------------------------------------------------------------------------------------
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }


# ------- TEMPLATE SETTINGS -------
# Configuration for Django templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True, # This setting enables Django to look for templates in the 'templates' directory of each app
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
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------- REST FRAMEWORK SETTINGS -------
# Configuration for the Django REST framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication', # This is the default authentication class for the Django REST framework
    )
}
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------- CHANNEL LAYERS SETTINGS -------
# Configuration for Django channels layers
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer", # This is the backend for the channel layer
        "CONFIG": {
            "hosts": [('localhost', 6379)], # This is the host and port for the Redis server (running as a Docker container)
        },
    },
}
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------- PASSWORD VALIDATION SETTINGS -------
# Configuration for password validation rules
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
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- ><
