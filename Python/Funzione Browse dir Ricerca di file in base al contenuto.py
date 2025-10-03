# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:22:54 2023

@author: mrchp
"""

# In[Ricerca di file in base al contenuto]
import os
def browse_dir( d, txt ):
    b = []
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path) and full_path.split('.')[-1] == 'py': #controllo estensione facendo un back -1 fino al punto
            f = open(full_path)
            for line in f:
                if txt in line:
                    b.append(full_path)
                    break
            f.close()
        elif os.path.isdir(full_path):
            c = browse_dir( full_path, txt=txt )
            b.extend(c)
    return b
  
b = browse_dir( os.getcwd(), 'len' )
print(b)