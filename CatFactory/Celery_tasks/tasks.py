import random
from decimal import Decimal
from django.db.models import F
from Company.models import Company
from CatFactory.celery import celery


@celery.task(bind=True)
def async_clear_debet(self, company_id):
    company = Company.objects.get(id=company_id)
    company.debet = 0
    company.save()


@celery.task
def increasing_debet():
    """
    Task to increase the debt for each company by a random amount between 5 and 500.
    """
    # Generate random increase sums for each company
    random_increase_sums = {
        comp.id: Decimal(random.randint(5, 500)) for comp in Company.objects.all()
    }
    # Update the debt for each company with the calculated increase sum
    for comp_id, random_increase_sum in random_increase_sums.items():
        Company.objects.filter(id=comp_id).update(debet=F('debet') + random_increase_sum)


@celery.task
def decreasing_debet():
    """
    Task to decrease the debt for each company by a random amount between 100 and 10000.
    If the resulting debt is negative, it is set to 0.
    """
    for comp in Company.objects.all():
        random_decrease_sum = Decimal(random.randint(100, 10000))
        new_debet_sum = comp.debet - random_decrease_sum
        if new_debet_sum < 0:
            comp.debet = 0
        else:
            comp.debet = new_debet_sum
        comp.save()
