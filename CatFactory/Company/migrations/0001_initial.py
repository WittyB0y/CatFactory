# Generated by Django 5.0.3 on 2024-03-30 10:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Contact', '0001_initial'),
        ('Product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_company', models.CharField(choices=[(1, 'Factory'), (2, 'Distributor'), (3, 'Dealership'), (4, 'Big Retail'), (5, 'Individual Entrepreneur')], max_length=50, verbose_name='Type of Company')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('debet', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Debet')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('contact_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Contact.contact')),
                ('product_id', models.ManyToManyField(blank=True, to='Product.product', verbose_name='Product id')),
                ('provider_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
                ('staff_id', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
            ],
        ),
    ]
