from django.core.serializers import deserialize
from celery import shared_task
from Company.models import Company
from CatFactory.celery import App


@App.task(bind=True)
def async_clear_debet(self, company_id):
    company = Company.objects.get(id=company_id)
    company.debet = 0
    company.save()
