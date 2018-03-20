#!/usr/bin/python
# -*- encoding: utf-8 -*-
emp_dict = {}

def get_emp():
    input_done = True
    while input_done:
        name = raw_input('输入雇员的名字，结束请输入Q：')

        if name.lower() == 'q':
            break

        number = raw_input('请输入员工编号：')

        emp_dict[name] = number

    print '原始数据为：',
    print emp_dict

def sorted_with_name():
    sorted_name = sorted(emp_dict.items(), key = lambda a:a[0])
    print sorted_name
    print dict(sorted_name)
def sorted_with_number():
    print sorted(emp_dict.items(),key = lambda b:b[1])

if __name__ =='__main__':
    get_emp()
    sorted_with_name()
    sorted_with_number()