# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default=None, upload_to='documents/%Y/%m/%d'),
        ),
    ]
