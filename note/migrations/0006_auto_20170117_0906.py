# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20170115_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '评论'},
        ),
        migrations.AlterField(
            model_name='note',
            name='tag',
            field=models.ManyToManyField(blank=True, to='note.Tag'),
        ),
    ]
