#!/usr/bin/env python
# encoding: utf-8
import os

def readfile():
    with open('bookmark.txt','r') as f:
        for line in f:
            line = line.rstrip('\n')
            print line

def addmark():
    whether = True
    while whether:
        name = raw_input('输入书签名字：')
        address = raw_input('输入URL地址：')
        bookmark = name + '-' + address
        with open('bookmark.txt','a+') as f:
            f.write(bookmark)
        whether_end = raw_input('输入结束请按q，继续请按c')
        if whether_end == 'q':
            whether = False

def modify():
    which_one = raw_input('输入需要修改的条目：')


