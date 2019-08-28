# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# Create your models here.

class Host(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=64, unique=True, verbose_name='主机名称')
    ipaddres = models.GenericIPAddressField(null=False, unique=True, verbose_name='ip地址')
    manage_user = models.ForeignKey(User, null=False,verbose_name='管理用户', related_name='admin',
                                    )
    port = models.SmallIntegerField(null=False,verbose_name='端口号',default=22)
    yewu = (
        ('app_yw', 'app业务'),
        ('h5_yw', 'H5业务'),
        ('www_yw', '官网业务'),
    )


    yw=models.CharField( choices=yewu,default='app_yw',max_length=40,verbose_name='业务类型',null=False)
    asset_type_choice = (
        ('server', '服务器'),
        ('networkdevice', '网络设备'),
        ('storagedevice', '存储设备'),
        ('securitydevice', '安全设备'),
        ('software', '软件资产'),
    )

    type_choice=models.CharField(choices=asset_type_choice,default='server',max_length=30,verbose_name='设备类型',null=False)

    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
    )

    status=models.SmallIntegerField(choices=asset_status,default=0,verbose_name='设备状态')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')

    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return  self.hostname      #注册到admin后显示为具体到列名，没有到话回显示object对象。
    class Meta:

        verbose_name='主机列表'      #注册到admin后台的表名
        db_table = 'addhost'
        ordering = ['-c_time']


class Spider(models.Model):
    id = models.AutoField(primary_key=True)
    site = models.CharField(max_length=64, unique=True, verbose_name='网站类型')
    error = models.CharField(max_length=64, unique=True, verbose_name='错误个数')
    success = models.CharField(max_length=64, unique=True, verbose_name='成功个数')
    kind = models.CharField(max_length=64, unique=True, verbose_name='错误格式')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')

    def __str__(self):
        return  self.site     #注册到admin后显示为具体到列名，没有到话回显示object对象。
    class Meta:

        verbose_name='爬虫统计'      #注册到admin后台的表名
        db_table = 'spider'
        ordering = ['-c_time']




