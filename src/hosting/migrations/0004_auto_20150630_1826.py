# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0003_auto_20150630_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosting',
            name='score',
            field=models.DecimalField(max_digits=5, default=0, decimal_places=2),
        ),
    ]
