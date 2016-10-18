# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_home_palavralink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='content',
            field=models.TextField(blank=True, verbose_name='Conteudo'),
        ),
        migrations.AlterField(
            model_name='home',
            name='description',
            field=models.CharField(blank=True, max_length=120, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='home',
            name='phrase',
            field=models.CharField(blank=True, max_length=120, verbose_name='Frase'),
        ),
        migrations.AlterField(
            model_name='home',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, verbose_name='Legenda'),
        ),
    ]
