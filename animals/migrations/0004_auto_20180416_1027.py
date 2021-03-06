# Generated by Django 2.0.4 on 2018-04-16 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20180416_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 4, 16, 10, 27, 42, 214307)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='modification_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='available_to',
            field=models.DateField(default=datetime.datetime(2018, 4, 30, 10, 27, 35, 202919)),
        ),
        migrations.AlterField(
            model_name='animal',
            name='entry_date',
            field=models.DateField(),
        ),
    ]
