# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(max_length=10000, verbose_name='内容')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('views', models.IntegerField(blank=True, default=1, verbose_name='浏览数')),
                ('poster_id', models.CharField(blank=True, default=1, max_length=100, verbose_name='作者')),
                ('original_url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': '学习笔记',
            },
        ),
    ]
