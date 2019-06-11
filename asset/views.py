from django.shortcuts import render
from  django.shortcuts import HttpResponse
from  models import Host


# Create your views here.


def asset_add(requests):


    return HttpResponse('hello word !')



def host_add(requests):


    return  render(requests, 'host_add.html', locals())


def index(requests):


    return  render(requests,'index.html',locals())



def host_list(requests):
    host_all=Host.objects.all()
    return  render(requests, 'host_list.html', locals())





