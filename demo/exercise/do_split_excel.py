#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_split_excel.py
@time: 2018/4/13 17:28
'''
__author__ = 'lierl'

import xlrd
import xlwt

limit = 10
readbook = "E:\\aaa.xlsx"
savebook = "e:\\files"
data = xlrd.open_workbook(readbook)
# 获取sheet
table = data.sheets()[0]

# 行数
nrows = table.nrows
# 列数
ncols = table.ncols

sheets = nrows / limit#总共需要多少excel

if not sheets.is_integer():
    sheets = sheets + 1

title_row = table.row_values(0)
#
for i in range(0, int(sheets)):
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(sheetname="0")
    for col in range(0,ncols):
        worksheet.write(0, col, title_row[col])
    for row in range(1, limit+1):#每次循环limit行
        newRow = row+limit*i
        if newRow < nrows:
            row_content = table.row_values(newRow)
            for col in range(0, ncols):
                worksheet.write(row, col, row_content[col])
    workbook.save(savebook+"\\"+str(i)+".xlsx")








