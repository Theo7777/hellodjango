# Django settings for myproject project.
import os.path
import socket

PROJECT_PATH =  os.path.dirname(os.path.abspath(__file__))

import socket

if socket.gethostname() == 'Theos-MacBook-Pro.local':
    DEBUG = TEMPLATE_DEBUG = True
else:
    DEBUG = TEMPLATE_DEBUG = False


DEFAULT_FROM_EMAIL = 'theo.ohene@gmail.com'
TEMPLATE_DEBUG = True

ADMINS = (
          ('Theo', 'theo.ohene@gmail.com'),
          )

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'theo.ohene@gmail.com'
EMAIL_HOST_PASSWORD = 'fowler77'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/Users/Theo/mydb.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
}
}



# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['lit-ridge-1114.herokuapp.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-GB'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
# MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"


AWS_STORAGE_BUCKET_NAME = 'theoohene'
#AWS_PRELOAD_METADATA = True # necessary to fix manage.py collectstatic command to only upload changed files instead of all files
AWS_ACCESS_KEY_ID = 'AKIAJ4DUFG5UHHDENCFA'
AWS_SECRET_ACCESS_KEY = '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'

# settings.py



# ...


if DEBUG:
    #Development storage using local files.
    STATIC_URL = '/static/'
    ADMIN_MEDIA_PREFIX = '/static/admin/'
else:
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = 'http://roundworld.s3.amazonaws.com/static/'



STATICFILES_DIRS = (
      #os.path.join(PROJECT_PATH, 'writer/static'),
      os.path.join(PROJECT_PATH, 'search/static'),
)

#ADMIN_MEDIA_PREFIX = 'https://theoohene.s3.amazonaws.com/static/admin/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')



# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
# STATIC_URL = '/static/'

# ADMIN_MEDIA_PREFIX = "/static/admin/"


#Additional locations of static files

# 
# STATICFILES_DIRS = (
#"/Users/Theo/hellodjango/writer/static"
#     )
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a-gtlqs9th*a(4o^chh$h(c6ttc3i22r7(xa77+@t@+!3a^+ct'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# AUTH_PROFILE_MODULE = 'login.Player'

ROOT_URLCONF = 'hellodjango.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'hellodjango.wsgi.application'


PROJECT_DIR = os.path.dirname(__file__) # this is not Django setting.
TEMPLATE_DIRS = (
                 os.path.join(PROJECT_DIR, "templates"),
                 # here you can add another templates directory if you wish.
                 )

#TEMPLATE_DIRS = (
#    '/Users/Theo/hellodjango/writer/templates',
#    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
#    # Always use forward slashes, even on Windows.
#    # Don't forget to use absolute paths, not relative paths.
#)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
    'writer', 
    #'storages',
    'search',
    'parallax',

   
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# # Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
