# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 22:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_usernotificationssettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderchat',
            name='contractor_last_read_at',
        ),
        migrations.RemoveField(
            model_name='orderchat',
            name='customer_last_read_at',
        ),
        migrations.RemoveField(
            model_name='orderchat',
            name='contractor_new_messages_count',
        ),
        migrations.RemoveField(
            model_name='orderchat',
            name='customer_new_messages_count',
        )
    ]