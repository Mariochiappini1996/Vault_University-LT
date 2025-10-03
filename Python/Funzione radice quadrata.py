# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:31:48 2023

@author: mrchp
"""

# In[]

def radice_quadrata( x, eps=0.01 ):
    # prima ipotesi
    g = x/2
    
    while abs( g*g - x ) > eps: # questo e' un ciclo
        g = 0.5 * ( g + x/g )

    return g

print(radice_quadrata(20, 0.000001))
print(radice_quadrata(20))
print(radice_quadrata(eps=0.000001, x = 90))
