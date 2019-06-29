# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:37:04 2019

@author: Aditya Tanwar
"""

 #to find second highest  NOT ACCURATE
n = int(input())
arr = map(int, input().split())
arr1=list(arr)
print(arr1)
arr2=sorted(arr1)
print(arr2)
print(arr2[-2])


 #to find second highest  ACCURATE
n = int(input())
arr = map(int, input().split())
arr1=list(arr)
arr2=sorted(arr1)
i=2
while arr2[n-1]==arr2[n-i]:
    if i<4:
        i=i+1
    else:
        break
print(arr2[n-i])