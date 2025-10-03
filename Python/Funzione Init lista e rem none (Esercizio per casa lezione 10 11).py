# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 10:22:26 2023

@author: mrchp
"""

"""
Esercizi per casa
Si progetti una funzione analoga a init_tuple per le liste.
Si progetti una funzione denominata init_tuple che prenda in input un intero positivo n e, 
opzionalmente, una funzione v. La funzione restituisca una tupla di lunghezza n che in posizione i contenga v(i).
Qualora il parametro v non fosse specificato, la funzione restituirebbe una tupla composta da n zeri.
Si progetti una funzione, denominata rem_none che prenda in input una lista ed elimini da questa tutti gli elementi a valore None.

def init_tuple(n, v = lambda x: 0 ):
    t = ()
    for i in range(n):
        # concateno (v(i), ) a t
        t += (v(i), ) # richiede i+2 operazioni
    return t

def init_tuple(n, v=None):
    if v == None:
        return (0, )*n
    t = ()
    for i in range(n):
        # concateno (v(i), ) a t
        t += (v(i), )
    return t

"""

def init_lista(n, v = lambda x: 0 ):
    t=[]
    for i in range(n):
        t.append(v(i))
        return t
    
print(init_lista(10, ))


# In[Esercizio per casa 2]

def rem_none( a ):
    i = 0
    while i < len(a):
        if a[i] == None:
            del(a[i])
        else:
            i += 1
    return a

b = [0, None, 1, None, 2, None]
b = rem_none(b)
print(b)
b = [0, None, None, None, 2, None]
b = rem_none(b)
print(b)
