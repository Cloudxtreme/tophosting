# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0002_hosting_old_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='hosting',
            name='avatar',
            field=models.ImageField(upload_to='hosting/avatar'),
        ),
        migrations.AlterField(
            model_name='hosting',
            name='logo',
            field=models.ImageField(upload_to='hosting/logo'),
        ),
        migrations.AddField(
            model_name='click',
            name='hosting',
            field=models.ForeignKey(to='hosting.Hosting'),
        ),
    ]
