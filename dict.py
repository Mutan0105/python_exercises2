#!/usr/bin/env python
# encoding: utf-8
d = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
number = raw_input("请输入数字")
a = []
i = 0
for i in number:

    a.append(d[i])
s ="-".join(list(a))
print s