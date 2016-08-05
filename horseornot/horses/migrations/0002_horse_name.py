# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='name',
            field=models.CharField(default='Twitter', max_length=50),
            preserve_default=False,
        ),
    ]
