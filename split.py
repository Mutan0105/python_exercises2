#!/usr/bin/env python
# encoding: utf-8
get_string = raw_input("请输入字符串：")
a = []
for i in get_string.split(" "):
    a.append(i)
b = "".join(a)
print b