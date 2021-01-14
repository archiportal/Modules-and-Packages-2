# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:47:43 2021

@author: ARCHISMAN ROY
"""

def f3(n):
    if(n==1):
        return 0  
    r=f3(n/2)+1
    return r