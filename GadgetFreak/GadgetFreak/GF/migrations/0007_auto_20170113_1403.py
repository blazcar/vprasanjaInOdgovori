# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GF', '0006_auto_20170113_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='GF.Article'),
        ),
    ]
