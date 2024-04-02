from django.core.management.base import BaseCommand
from faker import Faker

from CatFactory import settings
from Product.models import Product

TEST_DATA_SET = settings.TEST_DATA_SET


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker(["ru_RU", "en_US"])
        name = ['Iphone', 'Samsung', 'Xiaomi', 'Honor', 'Huawei', 'Vivo', 'Nokia',
                'ZTE', 'ASUS', 'ACER', 'Apple', 'Vision Pro', 'Google', 'Sony']
        product_model = ['2019', '2020', '2021', '2022', '2023', '2024', '1', '2', '3']
        for _ in range(0, TEST_DATA_SET):
            date_release = fake.date_between(start_date='-1y', end_date='+1y')
            Product.objects.create(
                name=fake.random_element(elements=name),
                product_model=fake.random_element(elements=product_model),
                date_release=date_release
            )
        self.stdout.write("Success: Products were added to DB!")
