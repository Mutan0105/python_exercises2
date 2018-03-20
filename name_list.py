#!/usr/bin/python
# -*- encoding: utf-8 -*-
i = 1
name_list = []

def input_check(name):
    global i
    wrong = []
    if ',' not in name:
        print '输入不规范，进行自动纠正'
        print '这是你第%d次输入错误' % i
        i += 1
        for n in name.split(' '):
            wrong.append(n)
        name = ",".join(wrong)
        return name

    else:
        return name


def get_name():
    input_ok = True
    j = 1

    while input_ok:
        print '输入第%s个名字，用"，"连接。输入完成请输Q' % j
        name = raw_input()
        if name == 'Q':
            break
        else:
            name = input_check(name)
            name_list.append(name)
            j += 1

    print name_list

def sort_name_list():
    name_list.sort()
    print '排序后的名单'
    for l in name_list:
        print l
if __name__ == '__main__':

    get_name()
    sort_name_list()