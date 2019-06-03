from django.shortcuts import render
from  django.shortcuts import HttpResponse

# Create your views here.


def asset_add(requests):


    return HttpResponse('hello word !')


def index(requests):


    return  render(requests,'index.html',locals())