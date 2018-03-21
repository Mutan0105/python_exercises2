#!/usr/bin/env python
# encoding: utf-8
import os
F = raw_input('pls input a file name:')
n = 0
f = open(F,'r')
for i in f:
    print i,
    n+=1
    if n==25:
        n=0
        a = raw_input('任意键继续')
f.close()