#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql
data=[("N4",55,"1963-04-03",10),
      ("N5", 56, "1963-04-04", 11),
      ("N6", 57, "1963-04-05", 12)]

#创建连接
mysql_connect=pymysql.connect(host="192.168.1.115",port=3306,user="yiruiduan",passwd="yiruiduan",db="oldboy")
#创建游标
cursor=mysql_connect.cursor()
# cursor.executemany("insert into student(name,age,register_date,id) values(%s,%s,%s,%s)",data)
# mysql_connect.commit()

cursor.execute("select * from student")
for line in cursor.fetchall():
      print(line)