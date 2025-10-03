# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:15:06 2023

@author: mrchp
"""

# In[]

def my_min_2( a ):
    '''

    Parameters
    ----------
    a : lista di lunghezza n

    '''
    m = a[0]
    for x in a:
        if x < m:
            m = x
    return m

a = [1,2,3,2,1,2,3,4]
print(my_min_2(a))

# In[]

def contavocali( a ):
    '''
    Input: a, stringa di lunghezza n
    '''
    #b = a[:]
    c = 0
    for x in b:
        if x in 'aeiouAEIOU':
            c += 1
    return c

b = 'python'
print(contavocali(b))

# In[]

def my_min_3( a, i = 0 ):
    if i == len(a)-1:
        return a[i]
    m = my_min_3(a, i+1)
    return m if m < a[i] else a[i]

b = [4,1,3,7,9]
print(my_min_3(a))
