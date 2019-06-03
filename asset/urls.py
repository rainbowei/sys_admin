# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 4:16 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : urls.py
# @Software: PyCharm
from  django.conf.urls import  url
import  asset.views as views

urlpatterns = [
    url('^add/',views.asset_add),
]




