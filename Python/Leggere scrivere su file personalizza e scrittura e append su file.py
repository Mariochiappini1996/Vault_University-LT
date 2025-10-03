# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:20:07 2023

@author: mrchp
"""

# In[Leggere e scrivere su file]

# caso Windows
a = 'C:\\Users\\Gianluca\\Dropbox\\teaching_and_work\\tv\\programmazione\\aa2022-23\\Programmazione-dei-Calcolatori-aa22-23\\15-2022-11-28\\lezioone_15.py'
# caso Linux/Unix
a = '/home/gianluca/Dropbox/teaching_and_work/tv/programmazione/aa2022-23/Programmazione-dei-Calcolatori-aa22-23/15-2022-11-28/lezione_15.py'

# personalizare a in base alle esigenze

f = open(a)

for line in f:
    print(line)
    
f.close()

# In[Scrittura e append su file]

f = open('prova_scrittura.txt', 'w')
f.write('prima riga\n')
f.write('seconda riga')
f.close()
f = open('prova_scrittura.txt', 'a')
f.write('\nprima riga\n')
f.write('seconda riga')
f.close()
