# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from asset.models import Host
from asset import host_form
from  asset import  tasks
from  django.http import JsonResponse
from asset.celery_form  import Celery_form


# Create your views here.


def host_add(requests):
    form = host_form.HostModelForm()

    if requests.method == "GET":
        return render(requests, 'host_add.html', locals())
    form = host_form.HostModelForm(data=requests.POST)
    if form.is_valid():
        form.save()
        return redirect('/asset/host_list/')
    return render(requests, 'host_add.html', locals())


def host_edit(requests, nid):
    obj = Host.objects.filter(id=nid).first()
    if requests.method == "GET":
        form = host_form.HostModelForm(instance=obj)

        return render(requests, 'host_add.html', locals())

    form = host_form.HostModelForm(data=requests.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/asset/host_list/')
    return render(requests, 'host_add.html', locals())


def host_del(requests, nid):
        Host.objects.filter(id=nid).delete()
        return redirect('/asset/host_list/')



def index(requests):
    total = float(Host.objects.count())
    upline = Host.objects.filter(status=0).count()
    dowline = Host.objects.filter(status=1).count()
    unknow = Host.objects.filter(status=2).count()
    faild = Host.objects.filter(status=3).count()
    backup = Host.objects.filter(status=4).count()
    per_upline = round(upline / total * 100, 1)
    per_downline = round(dowline / total * 100, 1)
    per_unknow = round(unknow / total * 100, 1)
    per_faild = round(faild / total * 100, 1)
    per_backup = round(backup / total * 100, 1)
    server_num = Host.objects.filter(type_choice='server').count()
    network_num = Host.objects.filter(type_choice='networkdevice').count()
    store_num = Host.objects.filter(type_choice='storagedevice').count()
    sec_num = Host.objects.filter(type_choice='securitydevice').count()
    soft_num = Host.objects.filter(type_choice='software').count()

    return render(requests, 'index.html', locals())


def host_list(requests):
    host_all = Host.objects.all()
    return render(requests, 'host_list.html', locals())




def do_task(request,*args,**kwargs):
     res=tasks.add.delay(1,2)

     return JsonResponse({'status': 'successful', 'task_id': res.task_id})






from django_celery_beat.models import PeriodicTask,IntervalSchedule


def  test(requests):
    if requests.method == "POST":
        form = Celery_form(requests.POST)
        if form.is_valid():

            return redirect('/')
    else:
        form = Celery_form()
    return render(requests, 'celery_add.html', {'form': form})




        # schedule, created = IntervalSchedule.objects.get_or_create(
        #      every=10,
        #      period=IntervalSchedule.SECONDS,
        # )
        #
        # PeriodicTask.objects.create(
        #
        #     interval=schedule,
        #     name='Importing contact',
        #     task='sys_admin.tasks.add',
        #
        # )
        #
        # return  HttpResponse('ok')







