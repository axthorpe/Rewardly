# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='api_key',
            field=models.CharField(default=b'123456789', max_length=32),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='customer_id',
            field=models.CharField(default=b'123456789', max_length=25),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
