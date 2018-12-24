#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#Iteration 1:
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
        if word in list_of_words:
            frequency = list_of_words.count(word)
            frequency_tracker[word] = frequency

    sorted_dictionary = sorted(frequency_tracker.items(), key=lambda t: t[1], reverse=True)
    for item in sorted_dictionary:
        print(f"{item[0]}: {item[1]}")

        
        
        
        
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

    frequently_used_words_with_counter = [f"{word}: {count}" for word, count in counters]

    formatted_word_frequency = ''
    for word in frequently_used_words_with_counter:
        formatted_word_frequency += word + '\n'

    print(formatted_word_frequency)
