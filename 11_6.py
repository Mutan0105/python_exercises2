#!/usr/bin/env python
# encoding: utf-8
def printf(fmt, *var):
    print fmt % var


printf('%d-%s-%s', 2016, '01', '06')