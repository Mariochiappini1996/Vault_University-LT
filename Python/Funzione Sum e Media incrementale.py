# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:26:14 2023

@author: mrchp
"""
# In[]

def my_sum(a, k):
    somma = 0
    for i in range(k):
        somma += a[i]
    return somma
    

def media_incrementale( a ):
    '''
    Input: a una lista di numeri (float o int)
    Output: una lista b t.c b[i] contenga la media dei primi i+1 elementi di a
    '''
    b = []
    for i in range(len(a)):
        b.append( my_sum(a, i+1)/(i+1) )
    return b
a = [1,2,3,4,5,6]
print( media_incrementale(a) )





# In[Versione singola funzione]

def media_incrementale2( a ):
    '''
    Input: a una lista di numeri (float o int)
    Output: una lista b t.c b[i] contenga la media dei primi i+1 elementi di a
    '''
    b, somma = [], 0
    for i in range(len(a)):
        b.append( (somma+a[i])/(i+1) )
        somma += a[i]
    return b

a = [1,2,3,4,5,6]
print( media_incrementale2(a) )

