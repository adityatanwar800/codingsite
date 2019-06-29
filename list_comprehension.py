# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:24:43 2019

@author: Aditya Tanwar
"""
#list comprehension
x = int ( input()) 
y = int ( input())
z=int(input())
n = int ( input()) 
print( [ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1)if ( ( i + j + k) != n )])


