# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:34:03 2023

@author: mrchp
"""

def hist(h0, h1, *numbers):
    seg0, seg1, seg2 = 0, 0, 0
    for x in numbers:
        if x < h0:
            seg0 += 1
        elif x < h1:
            seg1 += 1
        else:
            seg2 += 1
    return seg0, seg1, seg2


i0, i1, i2 = hist(-7, 5, 3, 10, -4, 5, -12, 6, 0)

t = hist(0, 5, 3, 10, -4, 5, -12, 6, 0)

print(i0, i1, i2)
