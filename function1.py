# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:28:15 2021

@author: ARCHISMAN ROY
"""

def f1(x,y):
    if x>=y:
        return (f1(x-y,y)+1)
    else:
        return (f1(y-x,x)+1)
    