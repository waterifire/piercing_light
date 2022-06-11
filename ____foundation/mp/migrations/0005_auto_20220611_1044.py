# Generated by Django 2.2.12 on 2022-06-11 10:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0004_auto_20220610_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='verse',
            name='shown_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='verse',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 10, 44, 27, 852516, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='word',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 10, 44, 27, 851922, tzinfo=utc)),
        ),
    ]