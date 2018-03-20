#!/usr/bin/env python
# encoding: utf-8
orgin = {}
out_put = {}
a = []
b = []

def get_dict():
    input_done = True
    while input_done:
        dict_key = raw_input("输入字典的键，结束请输入q：")
        if dict_key == 'q':
            break
        dict_value = raw_input("输入字典的值：")
        if dict_value == 'q':
            break

        orgin[dict_key] = dict_value
        print orgin

def diandao_dict():
    for key in orgin:
        a.append(key)
    print a
    for value in orgin.values():
        b.append(value)
    print b
    print type(b)
    dict_lang = len(a)
    i = 0
    while i < dict_lang:
        out_put[b[i]] = a[i]
        i = i + 1
    print out_put
    print orgin
get_dict()
diandao_dict()