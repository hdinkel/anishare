# Generated by Django 2.0.4 on 2018-04-13 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='available_from',
            field=models.DateField(default=datetime.datetime(2018, 4, 13, 15, 22, 27, 141867)),
        ),
        migrations.AlterField(
            model_name='animal',
            name='available_to',
            field=models.DateField(default=datetime.datetime(2018, 4, 27, 15, 22, 27, 141940)),
        ),
        migrations.AlterField(
            model_name='animal',
            name='new_owner',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
