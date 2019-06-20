# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 4:39 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : tasks.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add():
    return 'test addddddd'


@shared_task
def mul(x, y):
    return x * y