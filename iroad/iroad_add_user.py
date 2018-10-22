#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import xlrd
import pymysql
import socks,socket,uuid

class Creat_dirver(object):
    def __init__(self,url,username,password):
        self.url=url
        self.username=username
        self.password=password

    def creat_driver(self):
        driver = webdriver.Chrome(r"F:\chrome\chromedriver.exe")
        driver.get(url)
        print(driver.title)
        elem_know = driver.find_element_by_id("messageModal_btn")
        elem_know.click()
        time.sleep(1)
        elem_user = driver.find_element_by_id("phone")
        elem_user.send_keys(username)

        elem_password = driver.find_element_by_id("psw")
        elem_password.send_keys(password)

        elem = driver.find_element_by_id("login")
        elem.click()
        time.sleep(1)
        return driver

class Chang_row(object):
    def __init__(self,dirver):
        self.dirver=driver

    def find_row(self,phone_num):
        elem_find = driver.find_element_by_id("userManager_tel")
        elem_find.clear()
        elem_find.send_keys(phone_num)
        elem_search = driver.find_element_by_id("userManager_searchbtn")
        elem_search.click()
        time.sleep(1)
    def delete_user(self):
        elem_delete=self.dirver.find_element_by_xpath('//*[@id="userManagerTable"]/tbody/tr/td[9]/a[3]')
        elem_delete.click()
        time.sleep(1)
        elem_delete_define=self.dirver.find_element_by_xpath('//*[@id="exitModal"]/div/div/div[3]/button[2]')
        elem_delete_define.click()
        time.sleep(2)

class User_in_mysql(object):
    def __init__(self, host, user, pwd, dbname):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbname = dbname
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '221.237.165.19', 8686, False, 'nc', '123')
        socket.socket = socks.socksocket

        self.conn = pymysql.connect(self.host, self.user, self.pwd, self.dbname, port=3306,
                               charset='utf8')
        self.cur = self.conn.cursor()

    def exist_user(self,table,field):

        self.cur.execute('select %s from %s'%(field,table))
        data = self.cur.fetchall()
        exist_user_list=[]
        for key in data:
            exist_user_list.append(key[0])
        socks.set_default_proxy()
        return exist_user_list

    def insert_user(self,sql,field_list):
        self.cur.execute(sql,field_list)

        socks.set_default_proxy()




def add_user(phone_num,region_id,user_password,user_name,unit,num):
    elem_know=driver.find_element_by_id("userManager_add")
    elem_know.click()
    time.sleep(2)
    elem_user=driver.find_element_by_id("addUser_tel")
    elem_user.send_keys(phone_num)
    elem_user=driver.find_element_by_id("addUser_region")
    elem_user.send_keys(region_id)
    time.sleep(1)
    elem_user.find_element_by_xpath("/html/body/ul[%s]"%num).click()
    elem_user=driver.find_element_by_id("addUser_pwd")
    elem_user.send_keys(user_password)
    elem_user=driver.find_element_by_id("addUser_pwd1")
    elem_user.send_keys(user_password)
    elem_user=driver.find_element_by_id("addUser_yname")
    elem_user.send_keys(user_name)
    elem_user=driver.find_element_by_id("addUser_regonname")
    elem_user.send_keys(unit)
    elem_know=driver.find_element_by_id("addUser_submit")
    elem_know.click()
    time.sleep(2)
    elem_on = driver.find_element_by_xpath('//*[@id="userManagerTable"]/tbody/tr[1]/td[9]/a[4]')
    elem_on.click()
    time.sleep(3)

def xsl_resolve(file_name):
    ExcelFile=xlrd.open_workbook(file_name)
    sheet_name1=ExcelFile.sheet_names()[0]
    sheet=ExcelFile.sheet_by_name(sheet_name1)
    user_list=[]
    for i in range(4,sheet.nrows):
        new_user={}
        new_user["unit"]=sheet.cell(i,1).value
        new_user["user_name"]=sheet.cell(i,0).value
        new_user["phone_num"]=str(int(sheet.cell(i,3).value))
        new_user["user_password"]=str(int(sheet.cell(i,4).value))
        new_user["user_account"]=sheet.cell(i,2).value
        user_list.append(new_user)
    return user_list

def exist_user(file_name):
    exist_user_list=[]
    with open(file_name,"r",encoding="utf-8") as file:
        for phone in file:
            exist_user_list.append(int(phone.strip()))
    return exist_user_list




if __name__=="__main__":

    filename="test.xlsx"
    url = "http://221.237.165.19:8081/iroad-service510000/pages/view/index.html#../page/UserManager.html"
    username = "admin"
    password = "admin"
    sql = "insert into business_user (uid,user_name,user_dept,user_account,user_tel,user_pwd) values(%s,%s,%s,%s,%s,%s)"
    user_list = xsl_resolve(filename)
    exist_user_obj=User_in_mysql("192.169.0.26","root","ccico62979928","IROAD510000")
    exist_user_list=exist_user_obj.exist_user("sys_user_info","tel_phone")
    # exist_user_list1 = exist_user_obj.insert_user("sys_user_info", "tel_phone")
    # print("\033[31;0m%s\033[0m"%exist_user_list1)
    # conn = pymysql.connect("192.169.0.26","root","ccico62979928","IROAD510000", port=3306,
    #                        charset='utf8')
    choose=input("您读取的文件是\033[31;1m%s\033[0m里面可能有已经注册的用户是否重置[y/n]:"%filename)
    driver_obj=Creat_dirver(url,username,password)
    driver=driver_obj.creat_driver()
    User_obj=Chang_row(driver)
    if choose=="y":
        for user_message in user_list:
            phone_num = user_message["phone_num"]
            region_id = "四川"
            user_password = "123456"
            user_name = user_message["user_name"]
            unit = user_message["unit"]

            if user_message["phone_num"] in exist_user_list:
                User_obj.find_row(phone_num)
                User_obj.delete_user()
                User_obj.find_row("")
                print("\033[31;1m%s-%s-%s-%s-%s\033[0m"%(phone_num,region_id,user_password,user_name,unit))
    num=2
    yw_exist_user_list=exist_user_obj.exist_user("business_user","user_tel")

    for user_message in user_list:
        phone_num = user_message["phone_num"].strip()
        region_id = "四川"
        user_password = "123456"
        user_name = user_message["user_name"].strip()
        unit = user_message["unit"].strip()
        user_uuid = str(uuid.uuid1())
        user_account = user_message["user_account"].strip()
        user_pwd = user_message["user_password"].strip()

        if phone_num not in exist_user_list:
            print(phone_num,region_id,user_password,user_name,unit)
            add_user(phone_num,region_id,user_password,user_name,unit,num)
            num+=1
        if phone_num not in yw_exist_user_list:
            exist_user_obj.insert_user(sql, (user_uuid, user_name, unit, user_account, phone_num, user_pwd))
        else:
            print("\033[31;1m%s---%s---%s---%s---%s---%s已存在！！!\033[0m" % (
                user_uuid, user_name, unit, user_account, phone_num, user_pwd))
    exist_user_obj.conn.commit()
    driver.quit()