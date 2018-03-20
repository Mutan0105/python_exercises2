#!/usr/bin/env python
# encoding: utf-8

num_str = raw_input('Enter a number: ')

num_num = int(num_str)

fac_list = range(1, num_num + 1)
print "Before:",fac_list

i = 0
deleted = []

while i < len(fac_list):

    if num_num % fac_list[i] == 0:
        deleted.append(fac_list[i])

    i = i + 1
for ch in deleted:
    fac_list.remove(ch)

print "After:", fac_list