from celery import shared_task
from django.conf import settings


@shared_task
def analyze_file():
    pass
