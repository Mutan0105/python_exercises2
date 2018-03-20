#!/usr/bin/python
# -*- encoding: utf-8 -*-
get_string = raw_input("请输入字符串：")
get_list = []

for i in get_string:
    get_list.append(i)
print get_list
get_list[::-1]
print get_list
b = "".join(get_list)
print get_string + b
