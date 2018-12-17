#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import csv
new_words = [words for words in csv.reader(open("text_file.txt", newline=''))]

line_one_split_list_of_words = [word.split() for word in new_words[0]]
line_two_split_list_of_words = [word.split() for word in new_words[1]]
total_list = line_one_split_list_of_words + line_two_split_list_of_words

string_of_words = ''
for words in total_list:
    for word in words:
        string_of_words += word + ' '

set_unique_words = set(string_of_words.split())
list_of_unique_words = [word for word in set_unique_words]

final_output = ''

for word in list_of_unique_words:
    if word in string_of_words:
        word_count = string_of_words.count(word)
        final_output += f"{word}: {word_count}\n"
print(final_output.strip())
