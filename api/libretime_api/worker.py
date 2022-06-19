import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "libretime_api.settings.prod")
os.environ.setdefault("LIBRETIME_CONFIG_FILEPATH", "/etc/libretime/config.yml")

app = Celery("worker")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
