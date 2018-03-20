#!/usr/bin/python
# -*- encoding: utf-8 -*-
dict7 = {'a':'apple','z':'zoo','b':'but','x':'xo'}
b =[]

print sorted(dict7.keys())

a = sorted(dict7.keys())

for i in a:
    print dict7[i]
    b.append(dict7[i])
print b
for h in b:
    print 'key = %s, value = %s' % (dict7[h], h)