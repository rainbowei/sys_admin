# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 6:14 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : celery_form.py
# @Software: PyCharm

from django import forms
from django.forms import fields


class Celery_form(forms.Form):
    name = fields.CharField(max_length=20,
                            min_length=6,
                            required=True,
                            label='名字',
                            error_messages={
                                'required': '用户名不能为空',
                                'min_length': '太短了',
                                'max_length': "太长了",
                            }
                            ),
    task = fields.CharField(max_length=20,
                            min_length=6,
                            required=True,
                            label='任务名',
                            error_messages={
                                'required': '用户名不能为空',
                                'min_length': '太短了',
                                'max_length': "太长了",
                            }),
    union = fields.CharField(max_length=20,
                             min_length=6,
                             required=True,
                             label='单位',
                             error_messages={
                                 'required': '用户名不能为空',
                                 'min_length': '太短了',
                                 'max_length': "太长了",
                             }),
    value = fields.CharField(max_length=20,
                             min_length=6,
                             required=True,
                             label='值',
                             error_messages={
                                 'required': '用户名不能为空',
                                 'min_length': '太短了',
                                 'max_length': "太长了",
                             }),
