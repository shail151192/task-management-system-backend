# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-29 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='status',
        ),
    ]
