# Generated by Django 2.2.12 on 2022-06-11 11:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0005_auto_20220611_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verse',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 11, 6, 54, 257321, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 11, 6, 54, 256694, tzinfo=utc)),
        ),
    ]