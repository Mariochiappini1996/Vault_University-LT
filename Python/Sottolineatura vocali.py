# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:22:36 2023

@author: mrchp
"""

# In[sottolineare vocali]

x = input('Digita una stringa: ')
sottolineatura = ''

p = 0
while p < len(x):
    # verifico se x[p] Ã¨ una vocale minuscola
    if x[p] in 'aeiouAEIOU':
        sottolineatura += '*'
    else:
        sottolineatura += ' '
    p += 1 # equivalente a p = p+1
    
print(x)
print(sottolineatura)




# In[istruzione for]

x = input('Digita una stringa: ')
sottolineatura = ''

for c in x:
    # verifico se c Ã¨ una vocale
    if c in 'aeiouAEIOU':
        sottolineatura += '*'
    else:
        sottolineatura += ' '
    
print(x)
print(sottolineatura)
