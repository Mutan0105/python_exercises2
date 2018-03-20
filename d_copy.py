#!/usr/bin/env python
# encoding: utf-8
get_string = raw_input("输入需要拷贝的字符串：")
get_list = []

for i in get_string:
    get_list.append(i)

var = get_list[::-1]
a = "".join(var)

print get_string + a
