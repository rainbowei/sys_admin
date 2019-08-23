# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 3:13 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : pycurl-tool.py
# @Software: PyCharm
import subprocess


def purge(url):
    result = subprocess.call('curl -I -X PURGE %s' % (url), shell=True)
    if result == 0:
        print  'ok'
    else:
        print  '%s is not find'%(url)

purge('http://www.baidu./')
