# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 21:55
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_orderchatmessage_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotificationssettings',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='usernotificationssettings',
            name='notify_on_email',
            field=models.BooleanField(default=False),
        ),
    ]
