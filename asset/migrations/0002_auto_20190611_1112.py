# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='status',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\x9c\xa8\xe7\xba\xbf'), (1, b'\xe4\xb8\x8b\xe7\xba\xbf'), (2, b'\xe6\x9c\xaa\xe7\x9f\xa5'), (3, b'\xe6\x95\x85\xe9\x9a\x9c'), (4, b'\xe5\xa4\x87\xe7\x94\xa8')]),
        ),
        migrations.AddField(
            model_name='host',
            name='type_choice',
            field=models.CharField(default=b'server', max_length=30, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'server', b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8'), (b'networkdevice', b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87'), (b'storagedevice', b'\xe5\xad\x98\xe5\x82\xa8\xe8\xae\xbe\xe5\xa4\x87'), (b'securitydevice', b'\xe5\xae\x89\xe5\x85\xa8\xe8\xae\xbe\xe5\xa4\x87'), (b'software', b'\xe8\xbd\xaf\xe4\xbb\xb6\xe8\xb5\x84\xe4\xba\xa7')]),
        ),
        migrations.AddField(
            model_name='host',
            name='yw',
            field=models.CharField(default=b'app_yw', max_length=40, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'app_yw', b'app\xe4\xb8\x9a\xe5\x8a\xa1'), (b'h5_yw', b'H5\xe4\xb8\x9a\xe5\x8a\xa1'), (b'www_yw', b'\xe5\xae\x98\xe7\xbd\x91\xe4\xb8\x9a\xe5\x8a\xa1')]),
        ),
    ]
