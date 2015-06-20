# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('logo', models.ImageField(upload_to='/hosting/logo/')),
                ('avatar', models.ImageField(upload_to='/hosting/avatar/')),
                ('affiliate_link', models.URLField()),
                ('review', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('price', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('features', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
