# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:30:17 2023

@author: mrchp
"""

# In[]

'''
progettare una funzione che prende in input due interi a e b con b > a e restituisce

a*(a+1)*(a+2)*...*(b-1)*b
'''

def fattoriale_generalizzato(a, b):
    m, p = 1, a
    
    while p <= b:
        m *= p # m = m*p
        p += 1
        
    return m

print(fattoriale_generalizzato(2, 6))

# In[funzione range]

def fattoriale_generalizzato(a, b):
    m = 1
    
    for p in range(a, b+1):
        m *= p
        
    return m

print(fattoriale_generalizzato(2, 6))
