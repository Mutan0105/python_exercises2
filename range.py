#!/usr/bin/python
# -*- encoding: utf-8 -*-
def isprime():
    number = int(raw_input('请输入数字：'))
    a=[]
    i = 2
    while i < number:
        for i in range(2,number):
            if number % i == 0:
                a.append(i)
                print i
                number = number / i
                print number

    print a
isprime()