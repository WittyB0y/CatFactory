# Generated by Django 5.0.3 on 2024-03-31 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0003_alter_company_provider_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='provider_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.company'),
        ),
    ]
