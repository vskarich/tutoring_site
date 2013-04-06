import os, sys
sys.path.append('/home/ubuntu/tutoring_site')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tutoring_site.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

