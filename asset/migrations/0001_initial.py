# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=64, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ipaddres', models.GenericIPAddressField(null=True, verbose_name=b'ip\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('port', models.SmallIntegerField(null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3\xe5\x8f\xb7', blank=True)),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f')),
                ('memo', models.CharField(max_length=128, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('manage_user', models.ForeignKey(related_name='admin', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe7\x94\xa8\xe6\x88\xb7', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['c_time'],
                'db_table': 'addhost',
                'verbose_name': '\u4e3b\u673a\u5217\u8868',
            },
        ),
    ]
