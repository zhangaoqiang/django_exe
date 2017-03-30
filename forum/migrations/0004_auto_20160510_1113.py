# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20160510_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True,
                                       verbose_name=b'\xe5\x9b\x9e\xe5\xb8\x96'
                                                    b'\xe6\x97\xb6\xe9'
                                                    b'\x97\xb4', null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='modify_time',
            field=models.DateTimeField(auto_now=True,
                                       verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9'
                                                    b'\xe6\x97\xb6\xe9'
                                                    b'\x97\xb4', null=True),
        ),
    ]
