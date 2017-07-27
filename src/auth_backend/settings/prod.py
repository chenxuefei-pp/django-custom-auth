# -*- coding:utf-8 -*-
'''
    Author : Xuefei Chen
    Email : chenxuefei_pp@163.com
    Created on : 2017/7/27 9:46
'''

from auth_backend.settings.base import *

###### MYSQL #####
MYSQL_HOST = os.getenv('DB_PORT_3306_TCP_ADDR') or 'localhost'
MYSQL_PORT = os.getenv('DB_PORT_3306_TCP_PORT') or '8888'
MYSQL_DBNAME = os.getenv('DB_ENV_MYSQL_DATABASE') or 'authdb'
MYSQL_USERNAME = os.getenv('DB_ENV_MYSQL_USER') or 'root'
MYSQL_PASSWORD = os.getenv('DB_ENV_MYSQL_PASSWORD') or '123456'


###### REDIS ######

REDIS_HOST = os.getenv('REDIS_PORT_6379_TCP_ADDR') or 'localhost'
REDIS_PORT = os.getenv('REDIS_PORT_6379_TCP_PORT') or 9999
REDIS_PREFIX = 'ab'


###### CACHE ######
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.backends.single.RedisCache',
        'LOCATION': '{0}:{1}'.format(REDIS_HOST,REDIS_PORT),
        'KEY_PREFIX': '{0}_cache'.format(REDIS_PREFIX),
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': '',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            }
        },
    },
}

##### SESSION #######
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = REDIS_HOST
SESSION_REDIS_PORT = REDIS_PORT
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = ''
SESSION_REDIS_PREFIX = '{0}_session'.format(REDIS_PREFIX)


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': MYSQL_DBNAME,
        'USER': MYSQL_USERNAME,
        'PASSWORD': MYSQL_PASSWORD,
        'HOST': MYSQL_HOST,
        'PORT':MYSQL_PORT,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static/media")

MEDIA_URL = '/static/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
]