# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-31 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20171229_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]