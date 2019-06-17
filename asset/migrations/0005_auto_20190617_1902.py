# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20190617_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='manage_user',
            field=models.ForeignKey(related_name='admin', verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='host',
            name='port',
            field=models.SmallIntegerField(default=22, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3\xe5\x8f\xb7'),
        ),
    ]
