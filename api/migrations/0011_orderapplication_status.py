# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170118_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderapplication',
            name='status',
            field=models.IntegerField(choices=[(0, 'NEW'), (1, 'ACCEPTED'), (2, 'DECLINED')], default=0),
        ),
    ]
