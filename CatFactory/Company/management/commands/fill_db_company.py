from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from CatFactory import settings
from Company.models import Company
from Contact.models import Contact, Address, Email
from Product.models import Product

TEST_DATA_SET = settings.TEST_DATA_SET


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker(["ru_RU", "en_US"])
        with transaction.atomic():
            for _ in range(TEST_DATA_SET):

                address = Address.objects.create(
                    country=fake.country(),
                    city=fake.city(),
                    street=fake.street_name(),
                    number=fake.building_number(),
                    zip_code=fake.zipcode()
                )

                email = Email.objects.create(email=fake.email())

                contact = Contact.objects.create(
                    address_id=address,
                    email_id=email
                )

                products = Product.objects.order_by('?')[:3]

                staff = User.objects.order_by('?')[:3]

                company = Company.objects.create(
                    level_company=fake.random_int(min=1, max=5),
                    name=fake.company(),
                    contact_id=contact,
                    debet=fake.random_number(digits=6),
                )
                company.product_id.set(products)
                company.staff_id.set(staff)
        self.stdout.write("Success: Companies were added to DB!")
