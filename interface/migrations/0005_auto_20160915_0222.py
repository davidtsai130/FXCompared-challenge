# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 02:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_auto_20160914_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 15, 2, 22, 24, 22941, tzinfo=utc)),
        ),
    ]
