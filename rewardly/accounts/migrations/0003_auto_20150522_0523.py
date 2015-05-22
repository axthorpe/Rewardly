# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150522_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='api_key',
            field=models.CharField(default=b'123456789', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='customer_id',
            field=models.CharField(default=b'123456789', max_length=50),
        ),
    ]
