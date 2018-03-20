#!/usr/bin/python
# -*- encoding: utf-8 -*-
o_string = []
get_con = raw_input("输入字符串")

get_string = raw_input("输入：")

number = 0

if get_string in get_con:
    for i in get_con.split(" "):
        o_string.append(i)

        number = o_string.count(get_string)

    print "重复%d次" % number

else:
    print "输入的字符串不包含在内"