#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlrd
toll_list1=[]
with open("河北收费站.txt","r",encoding="utf-8") as f:
    for line in f:
        if line.startswith("所属高速："):
            toll_list1.append(line.strip().split("：")[2].split("收")[0])
ExcelFile = xlrd.open_workbook("收费站名称汇总.xlsx")
sheet_name1 = ExcelFile.sheet_names()
# print(sheet_name1)
toll_list=[]
for sheet_name in sheet_name1:
    sheet = ExcelFile.sheet_by_name(sheet_name)
    for row in range(2,sheet.nrows):
        toll_list.append(sheet.cell(row,3).value.strip().split("收")[0])
        if sheet.cell(row,3).value.strip().split("收")[0] not in toll_list1:
            print(sheet.cell(row,3).value.strip().split("收")[0])
        # print(sheet.cell(row,3).value)
print(toll_list)