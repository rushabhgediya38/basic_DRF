# Generated by Django 3.1.7 on 2021-04-04 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Duration',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 8, 15, 42, 47126)),
        ),
    ]
