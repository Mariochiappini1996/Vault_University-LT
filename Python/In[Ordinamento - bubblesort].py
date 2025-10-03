# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:41:13 2023

@author: mrchp
"""

# In[ORDINAMENTO - BubbleSort]

a = [10, 1, 23, 4, 80, 9, 11, 4]

a = [1, 4, 4, 9, 100, 11, 23, 80]

# In[]



n = len(a)

for j in range(n-1):
    i = 0
    while i < n-1-j:
        if a[i] > a[i+1]:
            # se la lista Ã¨ ordinata non entro
            a[i], a[i+1] = a[i+1], a[i]
        i += 1

print(a, j)

# In[]

ordinata = False
j = 0

while not ordinata:
    ordinata = True
    i = 0
    while i < n-1-j:
        if a[i] > a[i+1]:
            # se la lista Ã¨ ordinata non entro
            a[i], a[i+1] = a[i+1], a[i]
            ordinata = False
        i += 1
    j += 1
        
print(a, j)