# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 4:25 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : refresh_form.py
# @Software: PyCharm
from  django import  forms
from django.core.validators import  URLValidator


class  refresh_url(forms.Form):
    urls= forms.URLField(
                min_length=16,  # 设置最小长度
              #  max_length=12,  # 设置最大长度
                label="地址",  # 设置标签名

                # 错误信息提示设置
                error_messages={
                    "min_length": "地址不能少16位",
                    "max_length": '地址不能超过12位',
                    "required": "地址不能为空"
                },
                # 插件设置
                widget=forms.widgets.TextInput(
                    attrs={"class": "form-control",'placeholder':"请输入要刷新的url地址",
                           'width':'500px'

                    }
                )
            )




