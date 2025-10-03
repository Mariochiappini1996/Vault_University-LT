# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:16:05 2023

@author: mrchp
"""

import os

def browse_dir( d, ext=None ):
    '''
    Input: d Ã¨ il nome di una cartella (un str), ext Ã¨ una str che indica
        una estensione di file
    Output: ritorna la lista di tutti i file in d e in tutte le sue sottocartelle che
        terminanano in .ext. Se ext==None, stampa tutti i file
    '''
    
    b = []
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path):
            if ext == None or x.split('.')[-1] == ext:
                b.append(full_path)
        elif os.path.isdir(full_path):
            c = browse_dir( full_path, ext=ext )
            b.extend(c)
            # equivalente a...
            #for x in c:
            #    b.append(x)
    return b
  
b = browse_dir( os.getcwd(), ext = 'py')
print(b)
