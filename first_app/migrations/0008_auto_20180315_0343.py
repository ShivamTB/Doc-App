# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 22:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_auto_20180315_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form3c',
            old_name='patient',
            new_name='pat',
        ),
    ]
