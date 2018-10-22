#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlwt
import re
workbook = xlwt.Workbook(encoding = 'ascii')
pattern = re.compile(u'[\u4e00-\u9fa5]+')


with open("河北北京天津收费站.txt","r",encoding="utf-8") as f:
    for line in f:
        if line.startswith("###"):
            filterdata = re.findall(pattern, line)
            worksheet = workbook.add_sheet(filterdata[0])
            worksheet.write(0,1,label="所属高速")
            worksheet.write(0, 2, label="高速名称")
            i=1
        if line.startswith("所属高速："):
            for j in range(3):
                # print(j)
                # print((line.strip().split("：")[j]))
                worksheet.write(i,j,label=line.strip().split("：")[j])
            i+=1
workbook.save("河北北京天津高速.xlsx")
