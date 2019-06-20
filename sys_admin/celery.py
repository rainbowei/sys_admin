# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 4:01 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : celery.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery,platforms
platforms.C_FORCE_ROOT = True


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sys_admin.settings')  # 设置django环境

app = Celery('sys_admin')

app.config_from_object('django.conf:settings', namespace='CELERY') #  使用CELERY_ 作为前缀，在settings中写配置

app.autodiscover_tasks()  # 发现任务文件每个app下的task.py