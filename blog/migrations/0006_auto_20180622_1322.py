# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161127_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='documents/%Y/%m/%d/%H%M'),
        ),
    ]
