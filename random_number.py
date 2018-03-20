#!/usr/bin/python
# -*- encoding: utf-8 -*-
import random

def set_random():
    Aset = set()
    Bset = set()
    temp = random.randint(1,10)
    for i in range(temp):
        Aset.add(random.randint(0,9))
    temp = random.randint(1,10)
    for i in range(temp):
        Bset.add(random.randint(0,9))
    print 'Aset is:',Aset
    print 'Bset is:',Bset
    return (Aset,Bset)

def set_check(Aset,Bset):
    for i in range(3):
        Cset = set(map(int,raw_input('Please input A|B:').split()))
        Dset = set(map(int,raw_input('Please input A&B:').split()))
        if Aset|Bset==Cset and Aset&Bset==Dset:
            print 'Accepted!'
            break
        else:
            print 'Wrong answer!'
    else:
        print 'Aset|Bset is:',Aset|Bset
        print 'Bset&Bset is:',Aset&Bset

if __name__ == '__main__':
    myset = set_random()
    set_check(myset[0], myset[1])