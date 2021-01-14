# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:55:16 2021

@author: ARCHISMAN ROY
"""
#fact defines factorial
def fact(n):
    res =1
    for i in range(1 , n +1):
        res*=i

    return res


def f5(n,r):
    if n==0 or r==0:
        return 1
    x= int((fact(n)/(fact(n-r)*fact(r))))
    return x