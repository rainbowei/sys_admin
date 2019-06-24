# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 6:14 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : celery_form.py
# @Software: PyCharm

from django import forms
from django.forms import fields, widgets


class Celery_form(forms.Form):
    name = fields.CharField(
        widget=widgets.Input(attrs={'class': 'form-control'}),
        max_length=20,
        min_length=6,
        required=True,
        label='任务名',
        error_messages={
            'required': '名字不能为空',
            'min_length': '太短了',
            'max_length': "太长了",
        })
    task = fields.CharField(
        widget=widgets.Input(attrs={'class': 'form-control'}),
        max_length=20,
        min_length=6,
        required=True,
        label='任务',
        error_messages={
            'required': '任务不能为空',
            'min_length': '太短了',
            'max_length': "太长了",
        })
    period = fields.CharField(
        widget=widgets.Input(attrs={'class': 'form-control'}),
        max_length=20,
        min_length=6,
        required=True,
        label='周期',
        error_messages={
            'required': '周期不能为空',
            'min_length': '太短了',
            'max_length': "太长了",
        })
    every = fields.CharField(
        widget=widgets.Input(attrs={'class': 'form-control'}),
        required=True,
        label='时间',
        error_messages={
            'required': '时间不能为空',
            'min_length': '太短了',
            'max_length': "太长了",
        })
