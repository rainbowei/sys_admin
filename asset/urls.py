# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 4:16 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : urls.py
# @Software: PyCharm
from  django.conf.urls import  url
import  asset.views as views

urlpatterns = [
    url('^index/',views.index),
    url('^host_add/', views.host_add),
    url('^host_list/', views.host_list),
    url('^host_edit/(\d+)/',views.host_edit)

]




