# Generated by Django 3.1.7 on 2021-04-05 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp1', '0006_auto_20210405_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Duration',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 5, 8, 59, 46, 997474)),
        ),
    ]
