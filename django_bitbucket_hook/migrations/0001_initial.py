# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hook',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('repo', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
            ],
        ),
    ]
