# Generated by Django 4.2.1 on 2023-05-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairkit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_code',
            field=models.TextField(default='20230524-ea4e677a-95b0-4000-874c-50a491435346'),
        ),
    ]
