# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 11:10:38 2023

@author: mrchp
"""

# Si scriva una funzione, denominata intersection, che prenda in input due dizionari d0
# e d1 e restituisca una lista contenente le chiavi che sono in d0 ed in d1.
# NB: Sono ammesse soltanto le strutture dati trattate e lezione ovvero list, tuple,
# dict e str.

def intersection(d0,d1):
    listakeys=[]
    for key in d0.keys():
        if key in d1:
            listakeys.append(key)
        return listakeys
    
intersect0={'a':1, 'b':2,'c':3}
intersect1={'a':3, 'b':5,'c':8}
print(intersection(intersect0, intersect1))