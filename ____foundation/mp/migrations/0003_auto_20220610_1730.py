# Generated by Django 2.2.12 on 2022-06-10 17:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0002_auto_20220610_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verse',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 17, 30, 11, 96350, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 17, 30, 11, 95789, tzinfo=utc)),
        ),
    ]
