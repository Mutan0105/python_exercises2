#!/usr/bin/env python
# encoding: utf-8
def findchar(string,char):
    lenth = len(string)
    a = []
    for k in string:
        a.append(k)
    for i in range(lenth):
        if string[i] == char:
            a[i] = "*"
    s = "".join(a)
    print s



if __name__ == "__main__":
    string = raw_input("字符串：")
    char = raw_input("字符：")
    findchar(string,char)