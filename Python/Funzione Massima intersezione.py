# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:31:03 2023

@author: mrchp
"""

# In[]

def massima_intersezione( x, y ):
    '''
    Input: x ed y sono due stringhe
    Output: restituire il carattere in x che Ã¨ il piÃ¹ frequente in y
    '''
    n_max, c_max = 0, None # soluzione parziale
    for c in x:
        # conta il numero di volte in cui c compare in y
        n_c = 0
        for c_y in y:
            if c_y == c:
                n_c += 1
        if n_c > n_max:
            n_max, c_max = n_c, c
    return c_max

a, b = 'ciao', 'ramarro marrone'
r = massima_intersezione(a, b)
if r != None:
    print(f'Il carattere di \'{a}\' che compare piÃ¹ volte in \'{b}\' Ã¨ \'{r}\'')
else:
    print(f'\'{a}\' e \'{b}\' non hanno caratteri in comune')
