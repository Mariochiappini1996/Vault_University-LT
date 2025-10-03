# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:16:23 2023

@author: mrchp
"""
def identita(x):
    return x

# In[]

def str_cmp(x, y, key=str):
    '''
    Input: x, y, due stringhe; key una funzione con input str
    Output: ritorna -1 se key(x) < key(y); 0 se key(x) Ã¨ uguale a key(y);
        +1 se key(y)< key(x)
    '''
    if key(x) < key(y):
        return -1
    if key(x) == key(y):
        return 0
    return 1


# In[]

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



print(str_cmp('Addio', 'addio', len))
print(str_cmp('Addio', 'addio', str))
print(str_cmp('Addio', 'addio', identita))
print(str_cmp('Addio', 'addio'))
