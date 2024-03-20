#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:18:07 2024

@author: leoboullot
"""

import os

directory = "/Users/leoboullot/Documents/Documents - Leo's Mac/CPES - 2ème année/Stage ENS/database/data_leo"

for direct in os.listdir(directory):
    dir_path = os.path.join(directory, direct)
    if os.path.isdir(dir_path):
        for filename in os.listdir(dir_path):
            if filename.endswith(".tex"):
                filepath = os.path.join(dir_path, filename)
                with open(filepath, "r", encoding="utf-8", errors = 'replace') as file:
                    content = ""
                    print (filepath)
                    for line in file:
                        if "\\begin{tabular}" in line:
                            content += "\\leavevmode\\pdfstartlink\n"
                            content += line + "\n"
                        elif "\\end{tabular}" in line:
                            content += line + "\n"
                            content += "\\pdfendlink\n"
                        else:
                            content += line + "\n"
                new_filepath = os.path.join(dir_path, filename + "v2")
                with open(new_filepath, "w") as new_file:
                    new_file.write(content)
