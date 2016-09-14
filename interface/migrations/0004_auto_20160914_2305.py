# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 23:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_auto_20160914_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_from_set', to='interface.Account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='account_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_to_set', to='interface.Account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 14, 23, 5, 40, 648403, tzinfo=utc)),
        ),
    ]
