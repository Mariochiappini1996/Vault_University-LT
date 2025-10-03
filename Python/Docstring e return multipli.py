# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:16:13 2023

@author: mrchp
"""

# In[Docstring e return multipli]

def massima_intersezione( x, y ):
    '''
    Input: x ed y sono due stringhe
    Output: restituire il carattere in x che Ã¨ il piÃ¹ frequente in y e la
        sua frequenza
    '''
    n_max, c_max = 0, None # unpacking
    for c in x:
        # conta il numero di volte in cui c compare in y
        n_c = 0
        for c_y in y:
            if c_y == c:
                n_c += 1
        if n_c > n_max:
            n_max, c_max = n_c, c
    return c_max, n_max

a, b = 'ciao', 'ramarro marrone'
c, n = massima_intersezione( a, b ) # unpacking
print(c, n)
