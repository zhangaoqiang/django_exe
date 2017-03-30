# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(default=10000, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('rich_text', ckeditor.fields.RichTextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('outline', models.CharField(max_length=30, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('is_verify', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleHistory',
            fields=[
                ('id', models.AutoField(default=10000, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('rich_text', ckeditor.fields.RichTextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('outline', models.CharField(max_length=30, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('version_num', models.CharField(max_length=30, blank=True)),
                ('article', models.ForeignKey(to='wiki.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleModify',
            fields=[
                ('id', models.AutoField(default=10000, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('rich_text', ckeditor.fields.RichTextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('outline', models.CharField(max_length=30, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_verify', models.BooleanField()),
                ('article', models.ForeignKey(to='wiki.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(default=10000, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='course',
            field=models.ForeignKey(to='wiki.Course'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
