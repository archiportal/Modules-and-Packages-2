# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:28:15 2021

@author: ARCHISMAN ROY
"""

def f1(x,y):
    if y<=x:
        return int(f1(x-y,y)) + 1

    return 1
    