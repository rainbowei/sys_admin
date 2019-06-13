# -*- coding: utf-8 -*-
from django.shortcuts import render
from  django.shortcuts import HttpResponse
from  models import Host



# Create your views here.


def asset_add(requests):


    return HttpResponse('hello word !')



def host_add(requests):


    return  render(requests, 'host_add.html', locals())


def index(requests):
    upline=Host.objects.filter(status=0).count()
    dowline=Host.objects.filter(status=1).count()
    unknow=Host.objects.filter(status=2).count()
    faild=Host.objects.filter(status=3).count()
    backup=Host.objects.filter(status=4).count()
    server_num=Host.objects.filter(type_choice='server').count()
    network_num=Host.objects.filter(type_choice='networkdevice').count()
    store_num=Host.objects.filter(type_choice='storagedevice').count()
    sec_num=Host.objects.filter(type_choice='securitydevice').count()
    soft_num=Host.objects.filter(type_choice='software').count()





    return  render(requests,'index.html',locals())



def host_list(requests):
    host_all=Host.objects.all()
    return  render(requests, 'host_list.html', locals())





