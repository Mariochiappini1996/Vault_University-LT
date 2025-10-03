# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:38:56 2023

@author: mrchp
"""

import os

def analizza_test( cartella ):
    '''
    Assumiamo che n sia la dimensione complessiva dei file da analizzare
    '''
    d = {}
    for filename in os.listdir(cartella):
        if filename.split('.')[-1] == 'csv':
            print(filename)
            # analizziamo filename
            filepath = os.path.join(cartella, filename)
            f = open(filepath)
            for line in f: # per ogni riga di tutti i file (per n volte)
                # elaborare line
                k, v = line.split(';') # unpacking
                v = int(v)
                if k in d:
                    d[k].append(v)
                else:
                    d[k] = [v]         
            f.close()
    return d

# ComplessitÃ  computazionale
#
# n*O(1) = O(n) operazioni, ovvero O(1) per ogni riga dei file analizzati
#d = analizza_test('/home/gianluca/Dropbox/teaching_and_work/tv/programmazione/aa2022-23/Programmazione-dei-Calcolatori-aa22-23/19-2022-12-12')
#d = analizza_test('19-2022-12-12')
d = analizza_test('.') # cartella corrente
print(d)

# In[Soluzione con metodo get NON USARE]
import os
def analizza_test1( cartella ):
    '''
    Assumiamo che n sia la dimensione complessiva dei file da analizzare
    '''
    d = {}
    for filename in os.listdir(cartella):
        if filename.split('.')[-1] == 'csv':
            print(filename)
            # analizziamo filename
            filepath = os.path.join(cartella, filename)
            f = open(filepath)
            for line in f: # per ogni riga di tutti i file (per n volte)
                # elaborare line
                k, v = line.split(';') # unpacking
                v = int(v)
                a = d.get(k, [])
                d[k] = a.append(v) # cosa c'Ã¨  che non va?
                
            f.close()
    return d
# ComplessitÃ  computazionale
#
# n*O(1) = O(n) operazioni, ovvero O(1) per ogni riga dei file analizzati

d = analizza_test1('.')
print(d)

# In[Soluzione con metodo get e punti valore mappa]

import os
def analizza_test2( cartella ):
    '''
    Assumiamo che n sia la dimensione complessiva dei file da analizzare
    '''
    d = {}
    mappa_punti_valori = {6:0.3, 7:0.4, 8:0.6, 9:1, 10:1.5}
    for filename in os.listdir(cartella):
        if filename.split('.')[-1] == 'csv':
            print(filename)
            # analizziamo filename
            filepath = os.path.join(cartella, filename)
            f = open(filepath)
            for line in f: # per ogni riga di tutti i file (per n volte)
                # elaborare line
                k, p = line.split(';') # unpacking
                p = int(p)                
                d[k] = d.get(k, 0) + mappa_punti_valori.get(p, 0)              
            f.close()
    return d
# ComplessitÃ  computazionale
#
# n*O(1) = O(n) operazioni, ovvero O(1) per ogni riga dei file analizzati

d = analizza_test2('.')
print(d)

# In[Versione senza dizionario]

# in sostituzione della struttura dati dizionario viene utilizzata una lista
# contenente coppie identificativo,voto raccolte in liste di due elementi 
import os
def analizza_test_dict_free( folder ):
    mappa_voto = [0, 0, 0, 0, 0, 0, 0.3, 0.4, 0.6, 1, 1.5]
    d = [] # lista di liste di due elementi, se [k, v] Ã¨ in d, v Ã¨ la valutazione
            # finale di k
    for filename in os.listdir(folder):
        fullpath = os.path.join(folder, filename)
        if os.path.isfile(fullpath) and filename.split('.')[-1] == 'csv':
            f = open(fullpath)
            print(filename)
            for line in f: # per n volte
                k, p = line.split(';')  # O(1)
                v = mappa_voto[int(p)]  # O(1)
                # cerca k in d
                trovato, i = False, 0   # O(1)
                while not trovato and i < len(d): # nel caso peggiore O(n)
                    if d[i][0] == k:
                        d[i][1] += v
                        trovato = True
                    i += 1
                if not trovato:
                    d.append([k, v])
    return d

d = analizza_test_dict_free('.')
print(d)


# ComplessitÃ  computazionale Ã¨ O(n**2)

