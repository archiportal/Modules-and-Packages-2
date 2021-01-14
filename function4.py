# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:52:17 2021

@author: ARCHISMAN ROY
"""

def f4(m,n):
    if(m==0 or ((m>=n) and n>=1)):
        return 1
    else:
        x=f4(m-1,n)+ f4(m-1,n-1)
        return x