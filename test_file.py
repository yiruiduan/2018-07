#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlrd,xlwt
workbook=xlrd.open_workbook("河北北京天津高速.xlsx")
sheet_name=workbook.sheet_names()[0]
sheet=workbook.sheet_by_name(sheet_name)
rows=sheet.nrows
cols=sheet.ncols
new_list=[]
for i in range(rows):
    new_list.append("%s,%s"%(sheet.row_values(i)[0],sheet.row_values(i)[1]))
print(new_list)
    # for j in range(cols):
    #     print(sheet.cell(i,j).value)
f=xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet1=f.add_sheet("test",cell_overwrite_ok=True)
num=0
for line in new_list:
    sheet1.write(num,0,line)
    num+=1
f.save("nihenhao.xlsx")