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

sheets = nrows / limit

if not sheets.is_integer():
    sheets = sheets + 1


workbook = xlwt.Workbook(encoding='ascii')

for i in range(0, int(sheets)):
    worksheet = workbook.add_sheet(0)
    for row in range(1, limit):
        row_content = table.row_values(limit)
        print(row_content)
        # for col in range(0, ncols):
        #     worksheet.write(row, col, row_content[col])
    # workbook.save(savebook+"\\"+str(i)+".xlsx")








