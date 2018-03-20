#!/usr/bin/python
# -*- encoding: utf-8 -*-
dict_a ={}
c = 1

def tr():
    strin = raw_input('请输入原始字符串：')
    srcstr = raw_input('请输入需要替换的目标字符：')
    dststr = raw_input('请输入替换内容：')

    for i in strin:
        global c
        dict_a[c] = i
        c = c + 1
    print dict_a


tr()