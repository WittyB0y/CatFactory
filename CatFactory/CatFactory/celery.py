import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CatFactory.settings")

App = Celery("CatFactory")
App.config_from_object("django.conf:settings", namespace="CELERY")
App.autodiscover_tasks()
App.conf.timezone = "Europe/Minsk"
