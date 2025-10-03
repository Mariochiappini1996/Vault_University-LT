# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:32:21 2023

@author: mrchp
"""

# In[Esempio: stampa verticale]
def print_v( *strings ):
    '''
    Input: un numero variabile di stringhe
    Stampa le stringhe in verticale, uno di fianco l'altra
    Restituisce: None
    
    Esempio print_v('ciao', 'python')
    
    cp
    iy
    at
    oh
     o
     n
    '''    
    
    r = 0 # numero di riga
    terminato = False
    while not terminato:
        terminato = True
        # definiamo la riga r
        riga_r = ''
        for a in strings:
            if len(a) > r:
                riga_r += a[r]
                terminato = False
            else:
                riga_r += ' '
        if not terminato:
            print(riga_r)
        r += 1
        
print_v('ciao', 'python', 'programmazione', 'java', 'c++')
