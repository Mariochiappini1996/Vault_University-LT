# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:29:21 2023

@author: mrchp
"""

#1) Python Sia a una lista che contiene k elementi di tipo int, k elementi di tipo float e k
# elementi di tipo str. Si scriva un frammento di codice Python che stampi k
# righe tali che la prima contienga il primo int seguito dalla prima str seguita
# dal primo float; la seconda riga mostri il secondo int, la seconda str e il
# secondo float… e così via fino alla k-esima riga che elenchi l’ultimo int,
# l’ultima str e l’ultimo float.
# Si calcoli la complessità computazionale della soluzione.

#In[Input: k int, k float, k str. Output: print il primo elemento di ogni riga in riga 1, in riga 2 i secondi elementi e cosi via fino a k esimo ].

int = (10, 20, 30, 40, 50)
float = (11.5, 12.3, 13.7, 14.8, 15.9)
str = ('dieci', 'venti', 'trenta', 'quaranta', 'cinquanta')

def kelementi(int, float, str):
    k = len(int)
    i = 0

    for i in range(k):
        print(int[i], float[i], str[i])

print(kelementi(int, float, str))