#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import paramiko
import os,time,re,smtplib,logging
from email.mime.text import MIMEText
from email.header import Header
import time
import datetime
from  tools.wei_mysql_class  import  my_mysql ,dbconfig


year=datetime.datetime.now().strftime('%Y')
mon=datetime.datetime.now().strftime('%m')
day=datetime.datetime.now() + datetime.timedelta(days=-1)
yes_day=day.strftime('%d')
# day=datetime.datetime.now().strftime('%d')
date=year + '年' + mon  + '月' + yes_day + '日'
#创建SSHClient 实例对象
ssh=paramiko.SSHClient()
#调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接远程机器，地址，端口，用户名密码
ssh.connect('10.100.6.11',22,'root','haodou-2020-NODE')
#创建目录；
# cmd = 'bash /root/check_spider.sh'
# ssh.exec_command(cmd)
# time.sleep(600)
www_error_baidu_cmd = 'cat /root/spider/www_error_baiduspider.log|wc -l'
ssh.exec_command(www_error_baidu_cmd)
m_error_baidu_cmd = 'cat /root/spider/m_error_baiduspider.log|wc -l'
ssh.exec_command(m_error_baidu_cmd)
www_success_baidu_cmd = 'cat /root/spider/www_success_baiduspider.log|wc -l'
ssh.exec_command(www_success_baidu_cmd)
m_success_baidu_cmd = 'cat /root/spider/m_success_baiduspider.log|wc -l'
ssh.exec_command(m_success_baidu_cmd)
www_error_360_cmd = 'cat /root/spider/www_error_360spider.log|wc -l'
ssh.exec_command(www_error_360_cmd)
m_error_360_cmd = 'cat /root/spider/m_error_360spider.log|wc -l'
ssh.exec_command(m_error_360_cmd)
www_success_360_cmd = 'cat /root/spider/www_success_360spider.log|wc -l'
ssh.exec_command(www_success_360_cmd)
m_success_360_cmd = 'cat /root/spider/m_success_360spider.log|wc -l'
ssh.exec_command(m_success_360_cmd)
www_error_sougo_cmd = 'cat /root/spider/www_error_sougospider.log|wc -l'
ssh.exec_command(www_error_sougo_cmd)
m_error_sougo_cmd = 'cat /root/spider/m_error_sougospider.log|wc -l'
ssh.exec_command(m_error_sougo_cmd)
www_success_sougo_cmd = 'cat /root/spider/www_success_sougospider.log|wc -l'
ssh.exec_command(www_success_sougo_cmd)
m_success_sougo_cmd = 'cat /root/spider/m_success_sougospider.log|wc -l'
ssh.exec_command(m_success_sougo_cmd)
www_error_yisou_cmd = 'cat /root/spider/www_error_yisouspider.log|wc -l'
ssh.exec_command(www_error_yisou_cmd)
m_error_yisou_cmd = 'cat /root/spider/m_error_yisouspider.log|wc -l'
ssh.exec_command(m_error_yisou_cmd)
www_success_yisou_cmd = 'cat /root/spider/www_success_yisouspider.log|wc -l'
ssh.exec_command(www_success_yisou_cmd)
m_success_yisou_cmd = 'cat /root/spider/m_success_yisouspider.log|wc -l'
ssh.exec_command(m_success_yisou_cmd)
#如果命令行跨行
# cmd='''echo '123
# 45678
# 90abc'
#  >myfile'''
# ssh.exec_command(cmd)
#获取命令行的执行结果
# cmd ='cat myfile'
stdin,stdout,stderr =ssh.exec_command(www_error_baidu_cmd)
stdin1,stdout1,stderr1 =ssh.exec_command(m_error_baidu_cmd)
stdin2,stdout2,stderr2 =ssh.exec_command(www_success_baidu_cmd)
stdin3,stdout3,stderr3 =ssh.exec_command(m_success_baidu_cmd)
stdin4,stdout4,stderr4 =ssh.exec_command(www_error_360_cmd )
stdin5,stdout5,stderr5 =ssh.exec_command(m_error_360_cmd )
stdin6,stdout6,stderr6 =ssh.exec_command(www_success_360_cmd)
stdin7,stdout7,stderr7 =ssh.exec_command(m_success_360_cmd)

www_error_baidu_count=stdout.read().decode('utf-8')
m_error_baidu_count=stdout1.read().decode('utf-8')
www_success_baidu_count=stdout2.read().decode('utf-8')
m_success_baidu_count=stdout3.read().decode('utf-8')
www_error_360_count=stdout4.read().decode('utf-8')
m_error_360_count=stdout5.read().decode('utf-8')
www_success_360_count=stdout6.read().decode('utf-8')
m_success_360_count=stdout7.read().decode('utf-8')
#www_error_sougo_count=stdout8.read().decode('utf-8')
#m_error_sougo_count=stdout9.read().decode('utf-8')
#www_success_sougo_count=stdouta.read().decode('utf-8')
#m_success_sougo_count=stdoutb.read().decode('utf-8')
#www_error_yisou_count=stdoutc.read().decode('utf-8')
#m_error_yisou_count=stdoutd.read().decode('utf-8')
#www_success_yisou_count=stdoute.read().decode('utf-8')
#m_success_yisou_count=stdoutf.read().decode('utf-8')


stdin,stdout,stderr =ssh.exec_command(www_error_sougo_cmd)
stdin1,stdout1,stderr1 =ssh.exec_command(m_error_sougo_cmd)
www_error_sougo_count=stdout.read().decode('utf-8')
m_error_sougo_count=stdout1.read().decode('utf-8')









stdin,stdout,stderr =ssh.exec_command(www_success_sougo_cmd)
stdin1,stdout1,stderr1 =ssh.exec_command(m_success_sougo_cmd)
stdin2,stdout2,stderr2 =ssh.exec_command(www_error_yisou_cmd)
stdin3,stdout3,stderr3 =ssh.exec_command(m_error_yisou_cmd)
stdin4,stdout4,stderr4 =ssh.exec_command(www_success_yisou_cmd)
stdin5,stdout5,stderr5 =ssh.exec_command(m_success_yisou_cmd)

www_success_sougo_count=stdout.read().decode('utf-8')
m_success_sougo_count=stdout1.read().decode('utf-8')
www_error_yisou_count=stdout2.read().decode('utf-8')
m_error_yisou_count=stdout3.read().decode('utf-8')
www_success_yisou_count=stdout4.read().decode('utf-8')
m_success_yisou_count=stdout5.read().decode('utf-8')


# print(stdout.read()+stderr.read())
# print(stdout.read().decode('utf-8')+stderr.read().decode('utf-8'))
#print(error_baidu_count)
#print(success_baidu_count)
#print(error_360_count)
#print(success_360_count)
#print(error_sougo_count)
#print(success_sougo_cmd)
#print(error_yisou_count)
#print(success_yisou_count)
ssh.close()

try:
        con=my_mysql(dbconfig)
        insert_sql="insert into spider_tj(site,error,success,tjdate,kind) value('www','19333','3444','2019-08-26','百度')"
        con.insert(insert_sql)
except Exception as error:
         print('插入数据库失败')



con = my_mysql(dbconfig)
sql = "select * from spider_tj limit  5 "
con.query(sql)
result=con.findall_row()
for row in result:
     id=row[0]
     site=row[1]
     error=row[2]
     success=row[3]
     datetj=row[4]
     kind=row[5]
     print  error




