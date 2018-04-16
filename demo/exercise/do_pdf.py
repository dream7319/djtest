#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_pdf.py
@time: 2018/4/16 19:52
'''
__author__ = 'lierl'

from reportlab.pdfgen import canvas

def generate_pdf():
    pdf = canvas.Canvas(filename="E:\\aa.pdf")
    pdf.drawString(0,0,'hello world')
    # pdf.drawPath()
    pdf.showPage()
    pdf.save()

generate_pdf()

