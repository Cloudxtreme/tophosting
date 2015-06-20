# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosting',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
