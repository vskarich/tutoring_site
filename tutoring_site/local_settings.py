# Django settings for tutoring_site project.
from settings import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

def _require_debug_false(request):
    from django.conf import settings
    return not settings.DEBUG

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': _require_debug_false
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
