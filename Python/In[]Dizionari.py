# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 17:03:27 2023

@author: mrchp
"""

# In[Dizionari]

d0 = {} # dizionario vuoto
d1 = { 'k0':6, 'k1':'python', 6:3.14 }

# lettura
print( d1['k1'] )
#print( d1['k9'] ) # non Ã¨ una chiave del dizionario, errore!

if 'k9' in d1:
    print( d1['k9'] )
else:
    d1['k9'] = 'cappanove'
    
print(d1)

d1[6] = 'sei'

print(d1)

del(d1[6])  # elimina l'elemento con chiave 6

print(d1)

d1['L'] = [1]

print(d1)

d1['L'].append(0)

print(d1)

print(len(d1))

d1['k2'] = 6

print(d1.keys(), d1.values())