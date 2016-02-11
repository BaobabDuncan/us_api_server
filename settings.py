'''
Created on Apr 26, 2011

@author: woosanguk
'''

import os

DOMAIN = 'localhost:8084'


DEBUG = True
TEMPLATE_DEBUG = True
PROFILE = False
USE_I18N = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ko'

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Seoul ROK'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

ROOT_URLCONF = 'urls'

ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',    
)

STATIC_PATH = {
    'css' : '/css',
    'img' : '/img',
    'js' : '/js',
}





