# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:59:01 2023

@author: mrchp
"""

import os

cartella = os.listdir() #printa la lista di tutte le cartelle e file contenuti nella cartella corrente

for x in cartella: 
    if os.path.isdir(x): #Se trova e seleziona una Directory e la stampa
        print(f'DIR : {x}')
    elif os.path.isfile(x): #se trova e selezione un file e la stampa
        print(f'FILE: {x}')

# In[Funzione ricorsiva estrazione e stampa cartelle da cartellacorrente ]

def browse_dir( d ):
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path):
            print(f'FILE: {full_path}')
        elif os.path.isdir(full_path):
            browse_dir( full_path )
            
browse_dir( os.getcwd() )

