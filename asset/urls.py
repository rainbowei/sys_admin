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
    url('^host_edit/(\d+)/',views.host_edit),
    url('^host_del/(\d+)/', views.host_del),
    url('task/',views.do_task),
    url('celery_add/', views.cellery_add),
    url('crontabs/', views.crontabs),
    url('crontab_list/', views.crontab_list),
    url('test/', views.test),
    url('refresh',views.refresh),



]




