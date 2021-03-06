import os
from datetime import timedelta

from configurations import Configuration, values


class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # SECURITY
    # ------------------------------------------------------------------------------
    SECRET_KEY = values.SecretValue()
    DEBUG = True

    # DOMAINS
    ALLOWED_HOSTS = values.Value('*')
    DOMAIN = values.Value('')

    # APP CONFIGURATION
    # ------------------------------------------------------------------------------
    DJANGO_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
    ]

    THIRD_PARTY_APPS = [
        'graphene_django',
        'django_extensions',
    ]

    LOCAL_APPS = [
        'apps.users',
    ]

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    # MIDDLEWARE CONFIGURATION
    # ------------------------------------------------------------------------------
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # MANAGER CONFIGURATION
    # ------------------------------------------------------------------------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = [
        ('Ilya Filimonov', 'admin@freeminds.group'),
    ]

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS

    # DATABASE CONFIGURATION
    # ------------------------------------------------------------------------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db',
        }
    }

    # GENERAL CONFIGURATION
    # ------------------------------------------------------------------------------
    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = 'UTC'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'en-us'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True

    # STATIC FILE CONFIGURATION
    # ------------------------------------------------------------------------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/staticfiles/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]

    # MEDIA CONFIGURATION
    # ------------------------------------------------------------------------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'

    # URL Configuration
    # ------------------------------------------------------------------------------
    ROOT_URLCONF = '.'.join(['config', 'urls'])

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = '.'.join(['config', 'wsgi', 'application'])

    # TEMPLATE CONFIGURATION
    # ------------------------------------------------------------------------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': STATICFILES_DIRS,
            'OPTIONS': {
                'debug': DEBUG,
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    # PASSWORD STORAGE SETTINGS
    # ------------------------------------------------------------------------------
    # See https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.BCryptPasswordHasher',
    ]

    # PASSWORD VALIDATION
    # https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
    # ------------------------------------------------------------------------------
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]

    # AUTHENTICATION CONFIGURATION
    # ------------------------------------------------------------------------------
    AUTHENTICATION_BACKENDS = [
        'graphql_jwt.backends.JSONWebTokenBackend',
        'django.contrib.auth.backends.ModelBackend',
    ]

    # Custom user app defaults
    # Select the correct user model
    AUTH_USER_MODEL = 'users.User'

    # Graphene
    GRAPHENE = {
        'SCHEMA': 'config.schema.schema',
        'MIDDLEWARE': [
            'graphql_jwt.middleware.JSONWebTokenMiddleware',
        ],
    }

    if DEBUG:
        GRAPHENE['MIDDLEWARE'] = [
            'graphene_django.debug.DjangoDebugMiddleware',
            'graphql_jwt.middleware.JSONWebTokenMiddleware',
        ]

    GRAPHQL_JWT = {
        'JWT_EXPIRATION_DELTA': timedelta(days=30),
        'JWT_AUTH_HEADER': 'authorization',
        'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    }


class Dev(Base):
    """
    The in-development settings and the default configuration.
    """
    DOTENV = os.path.join(Base.BASE_DIR, '.env')

    SECRET_KEY = values.SecretValue()


class QA(Base):
    """
    The in-quality-assurance settings.
    """
    pass


class Prod(Base):
    """
    The in-production settings.
    """
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    SECRET_KEY = values.SecretValue()
