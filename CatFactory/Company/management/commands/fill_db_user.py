from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from CatFactory import settings

TEST_DATA_SET = settings.TEST_DATA_SET


class Command(BaseCommand):
    USER_DATA = {
        TEST_DATA_SET+1: {
            "username": "admin",
            "email": "bobrovnik42@gmail.com",
            "password": "admin"
        }
    }

    def handle(self, *args, **kwargs):
        fake = Faker(["ru_RU", "en_US"])
        for _ in range(0, TEST_DATA_SET):
            username = fake.user_name()
            email = f"{username}@testcatfactory.com"
            password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
            self.USER_DATA[_] = {
                "username": username,
                "email": email,
                "password": password,
            }
        for i, user in self.USER_DATA.items():
            is_superuser = False
            if user["username"] in ("admin", ):
                is_superuser = True
            User.objects.create_user(
                username=user["username"],
                password=user["password"],
                email=user["email"],
                is_staff=True,
                is_active=True,
                is_superuser=is_superuser
            )
        self.stdout.write("Success: Users were added to DB!")
