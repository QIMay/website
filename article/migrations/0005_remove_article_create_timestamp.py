# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_create_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='create_timestamp',
        ),
    ]
