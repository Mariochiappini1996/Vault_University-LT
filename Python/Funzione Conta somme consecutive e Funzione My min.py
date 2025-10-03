# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:12:23 2023

@author: mrchp
"""

def conta_somme_consecutive(a):
    c = 0
    for x, y, z in zip(a[:-2], a[1:-1], a[2:]):
        if z == x+y:
            c += 1
            
    return c

a = [5,3,8,6,14]
print( conta_somme_consecutive(a) )
# In[]

def my_min( a, b ):
    if a < b:
        return a
    else:
        return b
    
t = (8,0)

print(my_min( t[0], t[1] ))
print(my_min( *t ))
