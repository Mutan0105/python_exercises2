#!/usr/bin/env python
# encoding: utf-8
def rot13(str):
    strlist=[]
    for s in str:
        if s.isalpha():
            strnum=ord(s)
            if (65<=strnum<78) or (97<=strnum<110):
                strlist.append(chr(strnum+13))
            elif (78<=strnum<=90) or (110<=strnum<=122):
                strlist.append(chr(strnum-13))
        else:
            strlist.append(s)
    return ''.join(strlist)
string='This is a short sentence.'
print rot13(string)