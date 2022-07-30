#!/usr/bin/env python 
# -*- coding:utf-8 -*-



import sys
import  math
import pickle
import pprint, pickle

print("go big or go home")
print('——————————————————')
print('|   python团队    |')
print('|😀😃🙂😀😀😀😀😀😀|')
print('——————————————————')

def f(n):
    a,b =0,1
    while b<n:
        print (b,end=" ")
        a,b=b,a+b
    print()

def f2(n):
    re=[]
    a,b=0,1

    while(b<n):
        re.append(b)
        a, b = b, a + b
    return re

def this_fail():

    return 1/0

if __name__ == '__main__':

    try:
        this_fail()
    except ZeroDivisionError as err:
        print("error,please hanld it!",err)