# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20160509_1518'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('process', models.FloatField(max_length=5, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe8\xbf\x9b\xe5\xba\xa6')),
                ('learning_time', models.FloatField(max_length=5, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe6\x97\xb6\xe9\x95\xbf')),
                ('course', models.ForeignKey(verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b', to='wiki.Course')),
                ('user', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VisitLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_agent', models.CharField(max_length=30, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8')),
                ('user_origin', models.CharField(max_length=300, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x88\x9d\xe5\xa7\x8b\xe7\x9a\x84URL')),
                ('user_refer', models.CharField(max_length=300, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe9\x87\x8d\xe5\xae\x9a\xe5\x90\x91\xe7\x9a\x84URL')),
                ('visit_time', models.DateTimeField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe8\xae\xbf\xe9\x97\xae\xe6\x97\xb6\xe9\x97\xb4')),
                ('visit_ip', models.GenericIPAddressField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe8\xae\xbf\xe9\x97\xaeip')),
                ('user', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
