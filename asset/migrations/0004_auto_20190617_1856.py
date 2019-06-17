# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20190612_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='ipaddres',
            field=models.GenericIPAddressField(unique=True, verbose_name=b'ip\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
