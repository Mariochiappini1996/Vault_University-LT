# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:57:42 2023

@author: mrchp
"""

# In[]
def bin_search( k, bins ):
 
    n = len(bins)+1 # numero di segmentio
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    lx, rx = 0, n-1
    trovato = False
    
    while not trovato:
        cx = (lx+rx)//2
        # cx Ã¨ il segmento mediano tra lx e rx
        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k >= bins[cx]:
            # a dx del segmento cx
            lx = cx+1
        else:
            rx = cx-1
    
    return cx


def hist( a, bins ):
    '''
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in v < bins[0]
        - h[n-1] = numero di elementi in v >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''
    
    n = len(bins)+1 # un numero costante (rispetto a n e m) di operazioni
    h = [0]*n       # circa n operazioni
    
    for k in a:
        i = bin_search(k, bins) # O(log n)
        h[i] += 1
        
    return h # un numero costante (rispetto a n e m) di operazioni

print( hist([1, 3, -8, 10, 12, 9], [0, 10, 20, 30]) )

# In[]

# In[]

def bin_search( k, bins ):
 
    n = len(bins)+1 # numero di segmentio
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    lx, rx = 0, n-1
    trovato = False
    
    while not trovato:
        cx = (lx+rx)//2
        # cx Ã¨ il segmento mediano tra lx e rx
        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k >= bins[cx]:
            # a dx del segmento cx
            lx = cx+1
        else:
            rx = cx-1
    
    return cx

def hist( a, bins = [ i*10 for i in range(10) ] ):
    '''
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in v < bins[0]
        - h[n-1] = numero di elementi in v >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''
    
    n = len(bins)+1 # un numero costante (rispetto a n e m) di operazioni
    h = [0]*n       # circa n operazioni
    
    for k in a:
        i = bin_search(k, bins) # O(log n)
        h[i] += 1
        
    return h # un numero costante (rispetto a n e m) di operazioni

print( hist([1, 3, -8, 10, 12, 9]) )



