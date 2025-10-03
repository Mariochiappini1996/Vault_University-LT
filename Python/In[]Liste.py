# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 09:24:07 2023

@author: mrchp
"""
# In[Liste]

a0 = [] #lista vuota
a1 = [9, 'python', (1,2), [], 3.14]
a2 = ['ciao']

# supporta: indicizzazione, slicing, concatenazione, ripetizione, funzione le

a3 = a1 +a2 #nuova lista richiede len(a1)+len(a2) operazioni elementari
a4 = a1*2 # nuova lista richiede 2*len(a1) operazioni elementari

print(a1, a2, a3) 

a2.append('mondo') # una operazione elementare

print(a2)

a2[0] = 'Ciao'

print(a2)

del(a2[0])

print(a2)

print(a4)

a4[2] = None

print(a4)

