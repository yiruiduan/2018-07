#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,xlwt,xlrd
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet("all", cell_overwrite_ok=True)
num=1
for road_name in os.listdir("D:\\工作文档\\河北高速节点\\road_relationship"):
    Workbook = xlrd.open_workbook("D:\\工作文档\\河北高速节点\\road_relationship\\%s"%road_name)
    Sheet_name = Workbook.sheet_names()[0]
    Sheet = Workbook.sheet_by_name(Sheet_name)
    for line in range(1, Sheet.nrows):
        i=0
        for element in Sheet.row_values(line):
            sheet.write(num,i,element)
            i+=1
        num+=1



book.save("toll_all.xlsx")

