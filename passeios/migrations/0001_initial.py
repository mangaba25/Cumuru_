# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPasseio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Categoria_Passeio',
                'verbose_name_plural': 'Categoria_Passeios',
            },
        ),
        migrations.CreateModel(
            name='Passeio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(blank=True, max_length=100, verbose_name='Identificador')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='cumuruxatiba/images', verbose_name='Imagem_1')),
                ('decription_1', models.CharField(blank=True, max_length=100, verbose_name='Descrição-1')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='cumuruxatiba/images', verbose_name='Imagem_2')),
                ('decription_2', models.CharField(blank=True, max_length=100, verbose_name='Descrição-2')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='cumuruxatiba/images', verbose_name='Imagem_3')),
                ('decription_3', models.CharField(blank=True, max_length=100, verbose_name='Descrição-3')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='cumuruxatiba/images', verbose_name='Imagem_4')),
                ('decription_4', models.CharField(blank=True, max_length=100, verbose_name='Descrição-4')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='E-mail')),
                ('contact', models.IntegerField(blank=True, verbose_name='Contato')),
                ('site', models.CharField(blank=True, max_length=100, verbose_name='Site')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passeios.CategoryPasseio', verbose_name='Categoria_Passeios')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Passeio',
                'verbose_name_plural': 'Passeios',
            },
        ),
    ]
