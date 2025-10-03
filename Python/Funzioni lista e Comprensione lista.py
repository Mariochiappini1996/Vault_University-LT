# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 17:00:34 2023

@author: mrchp
"""

# In[Funzione list]
t = (1,2,3,4)
a = list(t) # costo lineare
print(a)

b = list('python')
print(b)

c = list(range(10))
print(c)

# In[Comprensione di lista (list comprehension)]

a = [ i**2 for i in range(10) ]
print(a)
