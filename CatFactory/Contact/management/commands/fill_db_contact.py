from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from CatFactory import settings
from Contact.models import Email, Contact, Address

TEST_DATA_SET = settings.TEST_DATA_SET


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker(["ru_RU", "en_US"])
        with transaction.atomic():
            for _ in range(TEST_DATA_SET):
                country = fake.country()
                city = fake.city()
                street = fake.street_name()
                number = fake.building_number()
                zip_code = fake.zipcode()
                address = Address.objects.create(
                    country=country,
                    city=city,
                    street=street,
                    number=number,
                    zip_code=zip_code
                )

                email = fake.unique.email()
                email_obj = Email.objects.create(email=email)

                Contact.objects.create(
                    address_id=address,
                    email_id=email_obj
                )
        self.stdout.write("Success: Contacts(address, email) were added to DB!")
