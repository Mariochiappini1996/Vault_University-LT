# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:35:26 2023

@author: mrchp
"""

# In[esercizio 1]

def dizionario_iniziali( a ):
    '''
    Input: una lista di n stringhe
    Output: un dizionario d che mappa caratteri in liste di stringhe tale che
        se d[k] = b, b contiene tutte le stringhe in a che iniziano per k 
    '''
    d = {}              # O(1)
    for x in a:         # per n volte
        if x == '':     # O(1)
            continue # torno a testare la condizione del ciclo saltando
                    # la  parte restante del blocco
        k = x[0]        # O(1)
        if k in d:      # O(1)
            d[k].append(x) # O(1) lettura del dizionario + O(1) per append
        else:
            d[k] = [x]  # O(1) costo per creare la lista + O(1) per scrittura
                        # nel dizionario
    return d

a = ['python', 'for', 'codice', 'programma', '', 'input', 'while', 'for', 'in']
d = dizionario_iniziali(a)
print(d)
