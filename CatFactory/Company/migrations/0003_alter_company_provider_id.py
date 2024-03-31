# Generated by Django 5.0.3 on 2024-03-30 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_alter_company_level_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='provider_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='Company.company'),
        ),
    ]
