# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-06 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passeios', '0003_imagepasseio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passeio',
            name='contact',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nome'),
        ),
    ]
