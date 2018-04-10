#!/usr/bin/env python
# encoding: utf-8
x = [1,2,3]
y = ['a', 'b', 'c']
a = []
def zip_func(x, y):
    for i in range(len(x)):
        a.append((x[i],y[i]))
    print a

zip_func(x,y)
