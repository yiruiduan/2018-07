#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlrd,xlwt
from operator import itemgetter, attrgetter
import time
import re
def Toll_inroad(exclename,roadname):
    Toll_list=[]
    Workbook=xlrd.open_workbook(exclename)
    Sheet_name=Workbook.sheet_names()[0]
    Sheet=Workbook.sheet_by_name(Sheet_name)
    for line in range(1,Sheet.nrows):
        if Sheet.row_values(line)[3] == roadname:

            Toll_list.append(Sheet.row_values(line))
    return Toll_list

def Toll_process(toll_list,roadname):
    toll_name = sorted(toll_list, key=itemgetter(4),reverse=True)
    region_code="130000"
    time_stamp=''
    start_num=float(toll_name[0][4])
    for line in toll_name:
        line[13] =str(time_stamp)
        time_stamp=int(round(time.time() * 100000))
        time.sleep(0.01)
        line[0]=str(time_stamp)
        line[1]=region_code
        end_num=line[4]
        distance=start_num-end_num
        start_num=line[4]
        line[11]='%.2f' % distance

    toll_name = sorted(toll_list, key=itemgetter(4))
    road_code=""
    roadname_element=re.findall(r'[0-9]+|[a-z]+|[A-Z]+|[-]', roadname)
    zero_len=6
    for element in roadname_element:
        zero_len=zero_len-len(element)
    roadname_element.insert(1,"0"*zero_len)
    # print(roadname_element)
    new_road_name=''.join(roadname_element)
    num=1
    for line in toll_name:
        line[6]=line[8].split(",")[0]
        line[7]=line[8].split(",")[1]
        new_num='%04d' % num
        node_code="%s%s%s"%(region_code,new_road_name,new_num)

        line[2]=node_code
        line[14]=road_code
        road_code=node_code
        num += 1

    return toll_name

def Create_new_sheet(File_name,roadname,toll_list):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(road_name, cell_overwrite_ok=True)
    title_list=['uid','政区编码',
                '节点编码',
                '路线编码',
                '桩号',
                '节点名称',
                'point_lon',
                'point_lat',
                '经纬度',
                '节点类型 1-收费站 2-杻纽',
                '所属主体',
                '距离(km)',
                '每公里费率',
                '下一节点的uid',
                '路段编码',
                "半径 "]
    i=0
    for element in title_list:
        sheet.write(0,i,element)
        i+=1
    k=1
    for line in toll_list:
        j=0
        for argv in line:
            sheet.write(k,j,argv)
            j+=1
        k+=1


    book.save('road_relationship/%s.xlsx'%road_name)


if __name__== "__main__":
    File_name="河北高速节点表v7.xls"
    while True:
        road_name=input("请输入公路编码：")
        toll_name =Toll_inroad(File_name,road_name)
        # print(toll_name)
        new_toll_list=Toll_process(toll_name,road_name)
        for line in new_toll_list:
            print(line)
        Create_new_sheet(File_name,road_name,new_toll_list)
        choose=input("\033[1;32m按任意键继续！q退出\033[0m")
        if choose == "q":
            break