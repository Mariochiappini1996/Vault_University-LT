# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:36:04 2023

@author: mrchp
"""

# In[Aliasing e clonazione]

a = [10,10,10,5,5,0]
b = a # aliasing
c = a[:] # clonazione
b[1] = 'casa'
c[0] = None
print(a)
print(b)
print(c)

def make_none( a ):
    for i in range(len(a)):
        a[i] = None

make_none(a)
print(a)
print(b)
print(c)

