# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:39:33 2023

@author: mrchp
"""

def deep_count( a ):
    '''
    Input: una lista  o una tupla
    Output: il numero di 'int', 'float', 'str', 'bool' e 'None' in a ed in tutte
        le sue sottoliste o sottotuple annidate
    '''

    c = 0
    for x in a:
        if type(x) in (int, float, str, bool, type(None)):
            c += 1
        elif type(x) in (list, tuple):
            c += deep_count( x )
    return c

a = [ 2, [True, [1, 2.1], None], '94', (12, [None, ['tre', [4, ['1']], [False, [4,5]] ]] ), 0 ]
print(deep_count( a ))
