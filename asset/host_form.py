# -*- coding: utf-8 -*-
# @Time    : 2019/6/15 6:46 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : host_form.py
# @Software: PyCharm

from django.forms import ModelForm
from asset import models
from django import forms


class HostModelForm(ModelForm):
    class Meta:
        model = models.Host
        fields = "__all__"
        error_messages = {
            'hostname': {'required': "主机名不能为空", },
            'ipaddres': {'required': "ip地址不能为空", },
        }

        widgets = {
            'hostname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'主机名'}),
            'ipaddres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ip'}),
            'manage_user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理用户'}),
            'port': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ip'}),
            'yw':forms.Select(attrs={'class': 'form-control'}),
            'type_choice': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }