# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:24:23 2023

@author: mrchp
"""
# In[completo con break e slicing]

x = 'programmgrazione'
#y = 'gramma'
y = 'gram'

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


# In[]

x = 'programmgrazione'
#y = 'gramma'
y = 'grxa'



p, trovato = 0, False
while p <= len(x)-len(y) and not trovato: # modificato tenendo conto che possa aver successo...
    # verifico se y Ã¨ in x a partire da p
    q = 0
    while q < len(y) and x[p+q] == y[q]:
        q += 1
    if not (q < len(y) ):
        print(y + ' compare in posizione ' + str(p) + ' di ' + x)
        trovato = True
        
    p += 1
    
if not trovato:
    print('non esiste corrispondenza')
    
# In[]

x = 'programmgrazione'
#y = 'gramma'
y = 'gra'



p, trovato = 0, False
while p <= len(x)-len(y) and not trovato: # modificato tenendo conto che possa aver successo...
    # verifico se y Ã¨ in x a partire da p
    q = 0
    while q < len(y) and x[p+q] == y[q]:
        q += 1
    if not (q < len(y) ):
        trovato = True
        break # esce dal ciclo piÃ¹ interno
    p += 1
    
if not trovato:
    print('non esiste corrispondenza')
else:
    print(y + ' compare in posizione ' + str(p) + ' di ' + x)
    
    
# In[]

x = 'programmgrazione'
#y = 'gramma'
y = 'gra'

p = 0
while p <= len(x)-len(y): # modificato tenendo conto che possa aver successo...
    # verifico se y Ã¨ in x a partire da p
    q = 0
    while q < len(y) and x[p+q] == y[q]:
        q += 1
    if not (q < len(y) ):
        break # esce dal ciclo piÃ¹ interno
    p += 1
    
if not (p <= len(x)-len(y)):
    print('non esiste corrispondenza')
else:
    print(y + ' compare in posizione ' + str(p) + ' di ' + x)
