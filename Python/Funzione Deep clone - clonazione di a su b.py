# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:46:43 2023

@author: mrchp
"""

def deep_clone( a ):
    b = []
    for x in a:
        if type(x) == list:
            b.append(deep_clone(x))
        else:
            b.append(x)
    return b

a = [0, [1, 2], 3, [4, 5] ]
b = deep_clone(a)
print(b)
