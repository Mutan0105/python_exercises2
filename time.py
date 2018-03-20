#!/usr/bin/env python
# encoding: utf-8
def trans_time():
    x = int(raw_input("输入时间："))
    hour = x/60
    minutes = x%60
    result = str(hour) + ":" + str(minutes)
    print result

trans_time()