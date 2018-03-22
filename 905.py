#!/usr/bin/env python
# encoding: utf-8

f = open('25.txt','r')
for line in f:
    line = line.rstrip('\n')
    print line
f.close()