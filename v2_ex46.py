#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import csv

filename = 'text_file.txt'

string_of_words = ''

with open(filename, newline='') as csvfile:
    linereader = csv.reader(csvfile, delimiter=' ')
    for rows in linereader:
        for row in rows:
            string_of_words += row + ' '
            list_of_words = string_of_words.split()

unique_words = set(list_of_words)

for word in unique_words:
    frequency = string_of_words.count(word)
    final_output = f"{word}: {frequency}\n"
    print(final_output.strip())
