# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 3:13 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@163.com
# @File    : pycurl-tool.py
# @Software: PyCharm
import subprocess


def purge(url):
    try:
      result = subprocess.check_call('curl -I -X PURGE %s' % (url), shell=True)
      return  '刷新成功'

    except Exception  as error:
      return error


