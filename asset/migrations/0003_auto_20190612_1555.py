# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-12 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20190611_1112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='host',
            options={'ordering': ['-c_time'], 'verbose_name': '\u4e3b\u673a\u5217\u8868'},
        ),
    ]