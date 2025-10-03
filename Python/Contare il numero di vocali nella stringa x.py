# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:18:43 2023

@author: mrchp
"""

#In[esercizio: contare il numero di vocali nella stringa x]

x = input('Digita una stringa: ')

numero_vocali = 0
p = 0

while p < len(x):
    # verifico se x[p] Ã¨ una vocale minuscola
    if x[p] in 'aeiouAEIOU':
        numero_vocali = numero_vocali+1
        # oppure numero_vocali += 1
    p += 1 # equivalente a p = p+1
    
print('Il numero di vocali in '+x+' é¨ '+str(numero_vocali))
