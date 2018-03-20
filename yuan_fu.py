#!/usr/bin/python
# -*- encoding: utf-8 -*-

yuan = ['a','e','i','o','u']
fu = ['b','c','c','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
y = 0
f = 0
a = []
s = raw_input(u'输入句子：')
st = []
for x in s:
    st.append(x)
print st
for i in st:
    if i in yuan:
        y+=1
    elif i in fu:
        f+=1

for n in s.split(' '):
    a.append(n)
print len(a)

print '元音字母有%d个' % y
print '辅音字母有%d个' % f