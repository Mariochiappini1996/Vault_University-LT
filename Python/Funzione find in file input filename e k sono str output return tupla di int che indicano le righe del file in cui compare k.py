# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:50:22 2023

@author: mrchp
"""

def find_in_file(filename, k):
    '''
	Input: filename e k sono str, filename Ã¨ il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le righe del file in cui compare k  
	'''
    f = open(filename)    # O(1) ovvero costo costante
    lines = ()            # O(1) 
    r = 1 # riga corrente
    
    for line in f:         # eseguito O(n)
        if k in line:      # le len(line) Ã¨ O(1), O(1) operazioni 
            lines += (r, ) # Ã¨ O(len(lines))+1 
        r += 1
    
    f.close()         # O(1)
    return lines      # O(1)

t = find_in_file('lezione_17.py', 'lines')
print(t)


#  In[Stessa funzione, costo computazionale] 
def find_in_file( filename, k):
    '''
    Input: filename e k sono str, filename Ã¨ il nome di un file
    Output: una tupla ( (r0, c0), (r1, c1), ...) di coppie di interi che indicano le
        righe e le colonne del file in cui compare k. Per colonna si intende la posizione
        all'interno della riga  
    '''
    f = open(filename)    # O(1) ovvero costo costante
    lines = []            # O(1) 
    r = 1 # riga corrente
    
    for line in f:          # eseguito O(n)
        for c in range(len(line)-len(k)+1):
            # verificare se  k Ã¨ il line a partire dalla posizione c
            if k == line[c:c+len(k)]: # len(line)-len(k)+len(k)
                lines.append( (r, c+1) ) # O(1)
        r += 1
    
    f.close()         # O(1)
    return tuple(lines)      # nel caso peggiore O(n)

t = find_in_file('lezione_17.py', 'lines')
print(t)  
