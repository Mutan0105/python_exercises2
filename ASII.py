#!/usr/bin/python
# -*- encoding: utf-8 -*-

start = int(raw_input('输入启始数字：'))
end = int(raw_input('输入终止数字：'))

dec = [x for x in range(start,end+1)]
bin = [bin(x) for x in range(start,end+1)]
oct = [oct(x) for x in range(start,end+1)]
hex = [hex(x) for x in range(start,end+1)]
ASII = [chr(x) for x in range(start,end+1)]

number = len(dec)

print len(ASII)

print '----------------------------'
print '输入起始值：%d\n输入终止数字：%d' % (start,end)

if len(ASII) == 0:
    print 'DEC      BIN      OCT      HEX'
    for i in range(1,number):
        print '%d      %s      %s      %s' % (dec[i],bin[i],oct[i],hex[i])
else:
    print 'DEC      BIN      OCT      HEX     ASCII'
    for i in range(1,number):
        print '%d      %s      %s      %s      %s' % (dec[i],bin[i],oct[i],hex[i],ASII[i])
