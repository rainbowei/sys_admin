# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 7:26 PM
# @Author  : sunkewei
# @Email   : sunkeweimail@153.com
# @File    : backup.py
# @Software: PyCharm

import  pymysql
import  time


dbconfig={
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'passwd':'sunkewei',
    'db':'spider'
    }


class my_mysql:
         def __init__(self,dbconfig):
             self.conn = pymysql.connect(host=dbconfig['host'],
                                    port=dbconfig['port'],
                                    user=dbconfig['user'],
                                    passwd=dbconfig['passwd'],
                                    db=dbconfig['db'])
             self.cur=self.conn.cursor()



         def query(self,sql):
             self.cur.execute("SET NAMES utf8")
             result=self.cur.execute(sql)
             return   result



         def update(self,sql):
             self.cur.execute("SET NAMES utf8")
             result=self.cur.execute(sql)
             self.conn.commit()
             return   result

         def insert(self, sql):
             self.cur.execute("SET NAMES utf8")
             result = self.cur.execute(sql)
             self.conn.commit()
             return result

         def findall_row(self):
             return  self.cur.fetchall()

         def findone_row(self):
             return  self.cur.fetchone()


         def __del__(self):
             self.cur.close()
             self.conn.close()

         def close(self):
            self.__del__()







# for name in range(20,100):
#     str_name='web-'+str(name)
#     update="insert into web_host(hostname,ssh_port) value('%s',22)"%(str_name)
#     db.insert(update)



# sql="select * from spider_tj"

#
#
# db.query(sql)
# ret=db.findall_row()
# print(ret)






