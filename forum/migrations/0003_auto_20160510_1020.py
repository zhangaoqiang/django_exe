# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20160509_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=ckeditor.fields.RichTextField(
                verbose_name=b'\xe5\x9b\x9e\xe5\xb8\x96\xe5\x86'
                             b'\x85\xe5\xae\xb9'),
        ),
    ]
