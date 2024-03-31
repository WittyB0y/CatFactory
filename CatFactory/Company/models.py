from django.db import models
from Contact.models import Contact
from Product.models import Product
from django.contrib.auth.models import User


class Company(models.Model):
    LEVEL_OF_COMPANY = [
        (1, "Factory"),
        (2, "Distributor"),
        (3, "Dealership"),
        (4, "Big Retail"),
        (5, "Individual Entrepreneur")
    ]
    level_company = models.IntegerField(choices=LEVEL_OF_COMPANY, verbose_name="Type of Company")
    name = models.CharField(max_length=200, verbose_name="Name")
    contact_id = models.OneToOneField(Contact, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product, verbose_name="Product id", blank=True)
    staff_id = models.ManyToManyField(User, verbose_name="Employee", blank=True)
    provider_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    debet = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Debet", default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    @property
    def provider(self):
        """
        to get provider_id from Company object, calling provider
        """
        if self.provider_id:
            return self.provider_id
        return None

    def __str__(self):
        return f"{self.name} - {self.debet}$ - {self.date_created}"
