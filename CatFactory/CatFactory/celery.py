import os
from celery import Celery

from CatFactory import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CatFactory.settings")
celery = Celery("CatFactory")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.conf.timezone = settings.TIME_ZONE  # Europe/Minsk
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
