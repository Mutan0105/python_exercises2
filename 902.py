#!/usr/bin/env python
# encoding: utf-8
import os.path
filename = raw_input('输入文件名：')
line = int(raw_input('您要读取几行：'))

if os.path.exists(filename):
    f = open(filename,'r')
    lines = f.readlines()
    for i in range(line):
        print lines[i]
    f.close()
else:
    print '文件不存在'