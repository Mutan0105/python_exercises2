#!/usr/bin/env python
# encoding: utf-8
number = int(raw_input('请输入数字：'))
k = 2
a = []
while number != 1:
    if number % k == 0:
        a.append(k)
        number = number / k
    else:
        k = k + 1
print a


