#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlwt,xlrd
import pymysql
import socks,socket

def xsl_resolve(file_name):
    ExcelFile=xlrd.open_workbook(file_name)
    sheet_name1=ExcelFile.sheet_names()[0]
    sheet=ExcelFile.sheet_by_name(sheet_name1)
    user_list=[]
    for i in range(2,sheet.nrows):
        new_user={}
        new_user["phone_num"]=sheet.cell(i,1).value
        new_user["user_account"]=sheet.cell(i,3).value
        user_list.append(new_user)
    return user_list

class User_in_mysql(object):
    def __init__(self, host, user, pwd, dbname):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbname = dbname
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '221.237.165.19', 8686, False, 'nc', '123')
        socket.socket = socks.socksocket
        self.conn = pymysql.connect(self.host, self.user, self.pwd, self.dbname, port=3306,charset='utf8')
        self.cur = self.conn.cursor()

    def update_user(self,table,user_account,user_tel):
        sql = "UPDATE %s SET user_account = '%s' WHERE user_tel = %d" % (table,user_account,user_tel)
        print(sql)
        # self.cur.execute(sql)
        # self.conn.commit()
        try:
           # 执行SQL语句
           self.cur.execute(sql)
           # 提交到数据库执行
           self.conn.commit()
        except:
           # 发生错误时回滚
           self.conn.rollback()


if __name__=="__main__":
    account=xsl_resolve("四川APP用户修改绑定业务账号.xlsx")
    exist_user_obj=User_in_mysql("192.169.0.26","root","ccico62979928","IROAD510000")
    for user_account in account:
        exist_user_obj.update_user("business_user",user_account["user_account"],int(user_account["phone_num"]))
