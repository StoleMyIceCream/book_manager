# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20170111_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='book.Author'),
        ),
    ]
