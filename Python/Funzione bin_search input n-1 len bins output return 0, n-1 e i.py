# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:54:05 2023

@author: mrchp
"""

# In[Implementazione della ricerca binaria]


def bin_search( k, bins ):
    '''
    sia n-1 la lunghezza di bins, ritorna 0 se k < bins[0],
        n-1 se k >= bin[n-2], i se bins[i-1] <= k < bin[i]
    '''

    n = len(bins)+1
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    lx, rx = 0, n
    trovato = False
    
    while not trovato:
        cx = (lx+rx)//2
        # cx Ã¨ il segmento mediano tra lx e rx
        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k < bins[cx-1]:
            # a sx del segmento cx
            rx = cx-1
        else:
            lx = cx+1
    
    return cx

print( bin_search(7, [6, 8, 10] ) )

# In[]

# In[Implementazione della ricerca binaria]


def bin_search( k, bins ):
    '''
    sia n-1 la lunghezza di bins, ritorna 0 se k < bins[0],
        n-1 se k >= bin[n-2], i se bins[i-1] <= k < bin[i]
    '''

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

print( bin_search(12, [6, 10] ) )
