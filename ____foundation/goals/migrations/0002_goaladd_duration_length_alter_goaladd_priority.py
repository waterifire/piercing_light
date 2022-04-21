# Generated by Django 4.0.3 on 2022-04-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goaladd',
            name='duration_length',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='goaladd',
            name='priority',
            field=models.IntegerField(help_text='low(1), medium(2) or high(3)'),
        ),
    ]
