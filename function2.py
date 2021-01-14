# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:31:38 2021

@author: ARCHISMAN ROY
"""

def f2(n,r):
    if(n==0):
        return r
    elif(r==0):
       return r
    else:
        return (f2(n-1,r)+f2(n-1,r-1))