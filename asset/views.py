# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from asset.models import Host,Spider
from asset import host_form
from asset import tasks
from django.http import JsonResponse
from asset.celery_form import Celery_form
from tools import refresh_url
from asset import refresh_form
from django_celery_beat.models import PeriodicTask, IntervalSchedule


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


def do_task(request, *args, **kwargs):
    res = tasks.add.delay(1, 2)

    return JsonResponse({'status': 'successful', 'task_id': res.task_id})


from django_celery_beat.models import PeriodicTask, IntervalSchedule


def cellery_add(requests):
    form = Celery_form()

    if requests.method == "GET":
        return render(requests, 'celery_add.html', {'form': form})

    form = Celery_form(requests.POST)
    if requests.method == "POST":
        if form.is_valid():
            name = requests.POST.get('name').encode('utf-8')
            every = requests.POST.get('every').encode('utf-8')
            task = requests.POST.get('task').encode('utf-8')
            period = requests.POST.get('period').encode('utf-8')

            print  type(name), type(every), type(task), type(period)
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=every,
                period=period,
            )

            PeriodicTask.objects.create(

                interval=schedule,
                name=name,
                task=task,

            )

            return redirect('/asset/index')

    return render(requests, 'celery_add.html', {'form': form})


def crontabs(requests):
    return render(requests, 'crontab.html', locals())


def crontab_list(requests):
    return render(requests, 'crontab_list.html', locals())


def test(requests):
    return render(requests, 'spider_success.html', locals())


def refresh(requests):
    test = refresh_form.refresh_url()
    if requests.method == "GET":
        return render(requests, 'refresh.html', locals())

    if requests.method == "POST":
        test = refresh_form.refresh_url(requests.POST)
        if test.is_valid():
            re_url = test.cleaned_data['urls']
            result = refresh_url.purge(re_url)
    return render(requests, 'refresh.html', locals())


def spider(requests):
    if requests.method == "GET":
        spider_all =Spider.objects.all()

        return render(requests, 'spider.html', locals())
