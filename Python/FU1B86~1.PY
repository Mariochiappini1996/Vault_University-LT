# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 13:57:36 2023

@author: mrchp
"""
# Si scriva una funzione, denominata initial_to_substring, che prenda in input una
# stringa a e restituisca un dizionario che mappi ogni carattere c di a nella sottostringa più lunga di a che inizi per c.

def initial_to_substring(a):
    substring_dict = {}
    k = len(a)
    
    for i in range(k):
        substring = a[i:]
        substring_dict[a[i]] = substring
    
    return substring_dict

# Esempio di utilizzo
input_string = "programming"
result = initial_to_substring(input_string)
print(result)