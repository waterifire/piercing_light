# Generated by Django 4.0.3 on 2022-04-16 10:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0003_rename_duration_length_goaladd_deadline_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='goalAdd',
            new_name='goal',
        ),
    ]
