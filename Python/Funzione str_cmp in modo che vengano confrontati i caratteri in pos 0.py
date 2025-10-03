# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:42:48 2023

@author: mrchp
"""
'''
Esercizio: descrivere come utilizzare la funzione str_cmp in modo che vengano
confrontati i caratteri in posizione 0 di due
stringhe in input x e y. In particolare ritorna -1 se x[0] < y[0];
ritorna 0 se x[0] == y[0]; ritorna +1 altrimenti
'''

def identita(x):
    return x

def str_cmp(x, y, key=None):
    '''
    Input: x, y, due stringhe; key una funzione con input str
    Output: ritorna -1 se key(x) < key(y); 0 se key(x) Ã¨ uguale a key(y);
        +1 se key(y)< key(x)
    '''
        
    x0, y0 = (x, y) if key == None else (key(x), key(y)) # espressione condionale

    if x0 < y0:
        return -1
    if x0 == y0:
        return 0
    return 1


def primo_elemento(x):
    return x[0]

print(str_cmp('aio', 'addio', primo_elemento))
