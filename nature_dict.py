#!/usr/bin/python
# -*- encoding: utf-8 -*-
d = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
     11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
     18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
     80:'eighty',90:'ninty',100:'hundred',1000:'one-thousand'}

get_string = raw_input("请输入数字：")
number = int(get_string)


if number <= 20:
    b = d[number]
    print b

if 20 <number< 100:
    a = int(get_string[-1])
    dict_a = d[a]
    c = int(get_string[-2])*10
    dict_c = d[c]
    print dict_c +"-"+ dict_a

if 100 <= number <= 999:
    a = int(get_string[-1])
    dict_a = d[a]
    c = int(get_string[-2]) * 10
    dict_c = d[c]
    e = int(get_string[-3])
    dict_e = d[e]
    print dict_e + "-" + d[100] +" "+"and"+" "+ dict_c +"-"+ dict_a
    print "%s-%s and %s-%s" % (dict_e,d[100],dict_c,dict_a)