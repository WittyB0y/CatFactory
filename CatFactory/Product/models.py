from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    product_model = models.CharField(max_length=150)
    date_release = models.DateField()

    def __str__(self):
        return f"{self.name} | {self.product_model} | {self.date_release}"
