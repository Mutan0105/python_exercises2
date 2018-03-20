#!/usr/bin/env python
# encoding: utf-8
import os
f = open(r'c:\users\qjd\python_exercises\testtext.txt','r')
for eachline in f:
    if eachline.startswith('#'):
        continue
    elif '#' in eachline:
        loc = eachline.find('#')
        print eachline[:loc]
    else:
        print eachline

f.close()