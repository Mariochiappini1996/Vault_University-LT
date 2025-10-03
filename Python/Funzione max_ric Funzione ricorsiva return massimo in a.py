# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:43:30 2023

@author: mrchp
"""

def max_ric(a):
    '''
    Input: una lista di numeri
    Output: massimo in a
        La funzione deve essere ricorsiva
        non si deve usare la funzione max
    '''
    n = len(a)
    if n == 1:
        return a[0]
    else:
        m = max_ric(  a[1:] )
        if a[0] > m:
            return a[0]
        else:
            return m
        
b = [1,7,2]
print(max_ric(b))
