#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:36:24 2024

@author: leoboullot
"""

from os import getcwd, chdir

chdir ("Documents")
chdir ("Documents - Leo's Mac")
chdir("CPES - 2ème année")
chdir("Stage ENS")
chdir ("database")
chdir ("data_leo")
chdir("1801.00004")
print (getcwd())


with open ("Test.tex", "r+") as fichier :
    a=""
    for line in fichier : 
        if "\\begin{tabular}" in line : 
            a+=("\\leavevmode\\pdfstartlink\n")
            a+=(line+"\n")
        elif "\\end{tabular}" in line : 
            a+=(line+"\n")
            a+=("\\pdfendlink\n")
        else : 
            a+=(line+"\n")
            
            
with open ("Test2.tex", "w") as file : 
        file.write(a)
        