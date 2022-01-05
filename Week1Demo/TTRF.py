#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:34:00 2019

@author: jiangchang
"""
def sRemove(listL):
    
    A = [',', 
         '.',
         '\n',
         '\t',
         '"',
         '\n\n',
         ']',
         '[',
         '\\',
         ';',
         ':',
         '(',
         ')',
         '_',
         '+',
         '-',
         '=']
    
    
    for sig in A:
        dRemove(sig, listL) 
      

def dRemove(word, listL):
    leng = len(listL)
    idx = 0
    exist = False
    for i in range(leng):
        if listL[i][0] == word:
            idx = i
            exist = True
    if exist:
        listL.pop(idx)
        

