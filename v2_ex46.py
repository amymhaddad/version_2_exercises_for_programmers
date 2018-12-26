#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import csv
from collections import OrderedDict

filename = 'text_file.csv'

with open(filename, newline ='') as csvfile:
    linereader = csv.reader(csvfile, delimiter=',')
    string_of_words = ''
    for rows in linereader:
        for row in rows:
            string_of_words += row + ' '
            list_of_words = string_of_words.split()

    unique_words = set(list_of_words)

    frequency_tracker = {}
    for word in unique_words:
        frequency = list_of_words.count(word)
        frequency_tracker[word] = frequency

    frequencies = OrderedDict(sorted(frequency_tracker.items(), key=lambda t: t[1], reverse=True))

    for word, count in frequencies.items():
        astericks = '*' * count
        print(f"{word}: {astericks}")

#########
#Iteration 2:

import csv
from collections import Counter

filename = 'text_file.csv'

with open(filename, newline='') as csvfile:
    linereader = csv.reader(csvfile, delimiter=',')
    string_of_words = ''
    for rows in linereader:
        for row in rows:
            string_of_words += row + ' '
            list_of_words = string_of_words.split()

    counters = Counter(list_of_words).most_common()

    for word, number in counters:
        astericks = '*' * number
        print(f"{word}: {astericks}")
