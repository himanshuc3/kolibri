# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-11 04:07
from __future__ import unicode_literals

import morango.utils.uuids
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kolibriauth', '0005_auto_20170511_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceowner',
            name='id',
            field=morango.utils.uuids.UUIDField(primary_key=True, serialize=False),
        ),
    ]
