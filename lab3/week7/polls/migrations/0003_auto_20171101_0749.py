# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171024_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date poll was published'),
        ),
    ]
