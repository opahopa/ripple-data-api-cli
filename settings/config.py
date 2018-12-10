import os, sys
import logging.config
import configparser
import platform

# logging.basicConfig(format='%(levelname)s|%(asctime)s|%(module)s|%(funcName)s|%(lineno)d|%(message)s',
#                            datefmt="%d/%b/%Y %H:%M:%S" , filename='example.log', level=logging.DEBUG)
config = configparser.ConfigParser()

DATA_API = 'https://data.ripple.com/v2/'

if getattr(sys, 'freeze', False):
    # running as bundle (aka frozen)
    bundle_dir = sys._MEIPASS.replace('/settings', '')
else:
    # running live
    bundle_dir = os.path.dirname(os.path.abspath(__file__)).replace('/settings', '')

BASE_DIR_LOG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

driver_paths = {
    'chrome': f'{bundle_dir}/selenium/chromedriver'
}

# Logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR_LOG, 'influsearch.log'),
            'maxBytes': 1024 * 1024 * 1,  # 1MB
            'backupCount': 10,
            'formatter': 'simple'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s|%(asctime)s|%(module)s|%(funcName)s|%(lineno)d|%(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s|%(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}
logging.config.dictConfig(LOGGING)


DISTRIB = platform.linux_distribution()[0].lower()