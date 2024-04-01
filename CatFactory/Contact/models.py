from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.number}"

    class Meta:
        verbose_name_plural = "Addresses"  # For plural Address object


class Email(models.Model):
    email = models.EmailField(null=False)

    def __str__(self):
        return self.email


class Contact(models.Model):
    address_id = models.ForeignKey("Address", on_delete=models.PROTECT, verbose_name="Address id")
    email_id = models.ForeignKey("Email", on_delete=models.PROTECT, verbose_name="Email id")

    def __str__(self):
        return f"{self.email_id} - {self.address_id}"
