#!/usr/bin/env python
# encoding: utf-8
def Tax(number, tax):
    money = number * tax
    print '应该缴纳的税额为%d' % money


if __name__ == '__main__':
    number = int(raw_input('输入金额'))

    Tax(number, tax = 0.17)