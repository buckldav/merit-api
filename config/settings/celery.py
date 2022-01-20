from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
app = Celery('config')
app.conf.enable_utc = False
app.conf.update(timezone='US/Mountain')
app.config_from_object(settings, namespace='CELERY')
