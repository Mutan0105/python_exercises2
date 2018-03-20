#!/usr/bin/env python
# encoding: utf-8
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    list = []
    fib(n)
    for i in range(1, n + 1):
        list.append(fib(i))
    print list


if __name__ == "__main__":
    n = int(raw_input("请输入需要计算的个数："))
    print fib(n)
    fib_seq(n)