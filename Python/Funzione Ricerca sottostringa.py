# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:29:20 2023

@author: mrchp
"""

# In[funzioni]

def ricerca_sottostringa(x, y): # parametri formali
    p, trovato = 0, False
    while p <= len(x)-len(y) and not trovato: # modificato tenendo conto che possa aver successo...
        # verifico se y Ã¨ in x a partire da p
        if y == x[p:p+len(y)]:
            trovato = True
            break # esce dal ciclo piÃ¹ interno
        p += 1
        
    if not trovato:
        print('non esiste corrispondenza')
    else:
        print(y + ' compare in posizione ' + str(p) + ' di ' + x)

# In[invocazione della funzione]

a = 'gra'
ricerca_sottostringa('programmazione', a) # parametri attuali



ricerca_sottostringa('python', a)

# In[funzioni con return]

def ricerca_sottostringa(x, y): # parametri formali
    p, trovato = 0, False
    while p <= len(x)-len(y) and not trovato: # modificato tenendo conto che possa aver successo...
        # verifico se y Ã¨ in x a partire da p
        if y == x[p:p+len(y)]:
            trovato = True
            break # esce dal ciclo piÃ¹ interno
        p += 1
        
    if not trovato:
        return -1
    else:
        return p
    
