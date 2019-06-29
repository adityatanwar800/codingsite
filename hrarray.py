# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 01:38:27 2019

@author: Aditya Tanwar
"""

import numpy

n,m,p=map(int,input().split())
n=int(n)
m=int(m)
p=int(p)
a=p
b=p
while a>0:
    print(numpy.zeros((n,m),dtype=numpy.int))
    a=a-1
while b>0:
    print(numpy.ones((n,m),dtype=numpy.int))
    b=b-1


