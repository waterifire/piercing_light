# Generated by Django 2.2.12 on 2022-06-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_rename_goaladd_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
