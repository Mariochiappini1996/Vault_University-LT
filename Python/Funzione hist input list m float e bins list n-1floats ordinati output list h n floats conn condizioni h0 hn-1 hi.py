# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:46:48 2023

@author: mrchp
"""

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
    
    for v in a:
        # blocco ripetuto m volte
        
        # cerco il segmento per v
        i = 0      # un numero costante (rispetto a n e m) di operazioni 
        while i < n-1 and v >= bins[i]: #  nel caso peggiore n volte
            i += 1 # un numero costante (rispetto a n e m) di operazioni 
        h[i] += 1 # un numero costante (rispetto a n e m) di operazioni 
        
    return h # un numero costante (rispetto a n e m) di operazioni

print( hist([90, 90, 90, 90], [1, 2,3,4,5]) )
