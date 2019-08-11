from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tarefa_example.settings')

from django.conf import settings  # noqa

app = Celery('tarefa_example')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: ['tarefas.tasks'])
