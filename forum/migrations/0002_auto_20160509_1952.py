# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=ckeditor.fields.RichTextField(
                verbose_name=b'\xe5\xb8\x96\xe5\xad\x90'
                             b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(default=b'', max_length=100,
                                   verbose_name=b'\xe5\xb8\x96\xe5\xad\x90'
                                                b'\xe6\xa0\x87\xe9\xa2\x98',
                                   blank=True),
        ),
    ]
