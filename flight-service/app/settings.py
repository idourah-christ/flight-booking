
from pathlib import Path
import environ
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "*"
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # models
    'account',
    'flight',

    # third parties
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'corsheaders',
    'django_nose',
    'rest_framework_swagger',
    'coverage',
    'django_filters'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

IHM_LINK = 'http://localhost:3000'

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5000',
    'http://localhost:5000',
    'http://localhost:8005',
    'http://127.0.0.1:8005'
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW = True 

CORS_ALLOW_METHODS = [ 
    'DELETE',
    'GET',
    'POST',
    'PUT',
]
ROOT_URLCONF = 'app.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'app.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# if DEBUG is False:
#     import dj_database_url
 
#     db_from_env = dj_database_url.config(conn_max_age=600)
#     DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICTFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.UserAccount'

# djoser settings

# rest framework permissin 
# IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),

}
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}

DOMAIN = ("localhost:8100")

SITE_NAME = ("Booking")

DJOSER = {
    'LOGIN_FIELD':'email',
    'USER_CREATE_PASSWORD_RETYPE':True, # password confirmation
    'USERNAME_CHANGED_EMAIL_CONFIRMATION':True, # send an email to the user when username changes
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'SEND_CONFIRMATION_EMAIL':False, # send confirmation email when register 
    'SET_USERNAME_RETYPE':True,
    'SET_PASSWORD_RETYPE':True,
    'PASSWORD_RESET_CONFIRM_URL':'password/resest/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL':'email/resest/confirm/{uid}/{token}',
    'ACTIVATION_URL':'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL':False,
    'SERIALIZERS':{
        'user_create':'account.serializers.UserCreateSerializer',
        'user':'account.serializers.UserCreateSerializer',
        'user_delete':'djoser.serializer.UserDeleteSerializer'
    },
    'EMAIL': {
        'activation': 'customemail.email.ActivationEmail',
        'confirmation': 'customemail.email.ConfirmationEmail',
    },
}


FORMATTERS = (
    {
        "verbose":{
            "format":"{levelname} {asctime:s} {threadName} {thread:d} {module} {filename} {lineno:d} {name} {funcName} {process:d} {message}",
            "style":"{"
        },
        "simple":{
            "format":"{levelname} {asctime:s} {module} {filename} {lineno:d} {funcName} {message}",
            "style":"{"
        }
    },
)

HANDLERS = {
    "console_handler":{
        "class":"logging.StreamHandler",
        "formatter":"simple"
    },
    "filebase_handler":{
        "class":"logging.handlers.RotatingFileHandler",
        "filename":"{0}/logs/mobemboLog.log".format(BASE_DIR),
        "mode":"a",
        "encoding":"utf-8",
        "formatter":"simple",
        "backupCount":8,
        "maxBytes":1024 * 1024 * 8 # 8 MB
    },
    "filebase_handler_detailed":{
        "class":"logging.handlers.RotatingFileHandler",
        "filename":"{0}/logs/mobemboLogDetailed.log".format(BASE_DIR),
        "mode":"a",
        "encoding":"utf-8",
        "formatter":"verbose",
        "backupCount":5,
        "maxBytes":1024 * 1024 * 5 # 5MB
    }
}

LOGGERS = (
    {
        "django":{
            "handlers":["console_handler", "filebase_handler_detailed"],
            "level":"INFO",
            "propagate":False
        },
        "django.request":{
            "handlers":["filebase_handler"],
            "level":"WARNING",
            "propagate":False
        },
        "django.error":{
            "handler":["filebase_handler"],
            "level":"ERROR",
            "propagate":False
        }
    },
)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters":FORMATTERS[0],
    "handlers":HANDLERS,
    "loggers": LOGGERS[0]
}

