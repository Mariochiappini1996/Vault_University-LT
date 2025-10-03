# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:42:48 2023

@author: mrchp
"""
"""
Esercizi per casa
Si progetti una funzione denominata init_tuple che prenda in input un intero positivo n e, opzionalmente, una funzione v. La funzione restituisca una tupla di lunghezza n che in posizione i contenga v(i). Qualora il parametro v non fosse specificato, la funzione restituirebbe una tupla composta da n zeri.

Suggerimento. Potrebbe essere utile partire da una tupla vuota - si indica così () - e poi procedere per concatenazioni successive. A tal proposito si provi ad usare l'operatore + come si fa con le stringhe. Una tupla composta da un unico elemento e si definisce in questo modo (e, ).

Utilizzare la funzione init_tuple per creare una tupla contenente i primi 10 numeri dispari

Utilizzare la funzione init_tuple per creare una tupla contenente 10 stringhe non vuote di lunghezza crescente

Utilizzare la funzione init_tuple per creare una tupla contenente 10 tuple tali che la tupla in posizione i sia lunga 10 e contenga i in ogni posizione. Suggerimento: come per le stringhe, * sulle tuple è l'operatore di ripetizione.
"""
# In[Esercizio per casa]

def init_tuple(n, v=None):
    if v == None:
        return (0, )*n
    t = ()
    for i in range(n):
        # concateno (v(i), ) a t
        t += (v(i), )
    return t

# In[Seconda versione]

def init_tuple(n, v = lambda x: 0 ):
    t = ()
    for i in range(n):
        # concateno (v(i), ) a t
        t += (v(i), ) # richiede i+2 operazioni
    return t

t0 = init_tuple(10, str)
print(t0)
t1 = init_tuple(10)
print(t1)

# In[]

t2 = init_tuple(10, v = lambda k: 2*k+1)
print(t2)

t3 = init_tuple(10, v = lambda k: 'X'*(k+1))
print(t3)

t4 = init_tuple(10, v = lambda k: (k,)*10)
print(t4)

# In[]

t5 = t4 + t0
print(t0)

