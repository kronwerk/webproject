#!/usr/bin/python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.insert(0, os.path.split(os.path.dirname(__file__))[0])

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
