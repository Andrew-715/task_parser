"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import
import os
from celery import Celery

from task_parser.settings import INSTALLED_APPS


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_parser.settings')

app = Celery("parser_app")

app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks(lambda: INSTALLED_APPS)
