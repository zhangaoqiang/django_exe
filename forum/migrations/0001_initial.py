# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0002_auto_20160506_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),

                ('content', ckeditor.fields.RichTextField(
                    verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),

                ('create_time',
                 models.DateTimeField(null=True,
                                      verbose_name=b'\xe5\x9b\x9e\xe5\xb8\x96'
                                                   b'\xe6\x97\xb6\xe9'
                                                   b'\x97\xb4')),

                ('modify_time',
                 models.DateTimeField(null=True,
                                      verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9'
                                                   b'\xe6\x97\xb6\xe9\x97'
                                                   b'\xb4')),

                ('reply_self',
                 models.ForeignKey(
                     verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe5'
                                  b'\x9b\x9e\xe5\xb8\x96',
                     blank=True, to='forum.Reply', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100,
                                           verbose_name=b'\xe5\x8f\x91\xe5\xb8'
                                                        b'\x96\xe6\xa0\x87\xe9'
                                                        b'\xa2\x98',
                                           blank=True)),
                ('content',
                 ckeditor.fields.RichTextField(
                     verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('modify_time',
                 models.DateTimeField(auto_now=True,
                                      verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9'
                                                   b'\xe6\x97\xb6\xe9\x97\xb4',
                                      null=True)),
                ('create_time',
                 models.DateTimeField(auto_now_add=True,
                                      verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba'
                                                   b'\xe6\x97\xb6\xe9\x97\xb4',
                                      null=True)),
                ('course',
                 models.ForeignKey(
                     verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe8\xaf\xbe'
                                  b'\xe7\xa8\x8b',
                     to='wiki.Course')),
                ('user',
                 models.ForeignKey(
                     verbose_name=b'\xe5\x8f\x91\xe5\xb8\x96\xe4\xba\xba',
                     to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_topic',
            field=models.ForeignKey(
                verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xb8\x96'
                             b'\xe5\xad\x90',
                blank=True, to='forum.Topic', null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(
                verbose_name=b'\xe5\x8f\x91\xe5\xb8\x96\xe4\xba\xba',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
