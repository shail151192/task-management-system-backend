# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-29 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20171229_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_on',
            field=models.DateTimeField(null=True),
        ),
    ]
