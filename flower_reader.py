#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

FILENAME = 'flowers.txt'
USER_NAME = input('Enter your first and last name: ')
FLOWERS = {}
FIND_FIRST_LETTER_OF_USER_NAME = lambda USER_NAME: USER_NAME[0].title()

def create_flower_dictionary(FILENAME):
    """Read in a file and create a dictionary"""

    list_of_flowers = []
    with open(FILENAME) as f_object:
        contents = f_object.readlines()
        for flower in contents:
            split_flower_content = flower.split(" ", 1)
            list_of_flowers.append(split_flower_content)

        for flower_types in list_of_flowers:
            letter = flower_types[0]
            flower_name = flower_types[1]
            FLOWERS[letter] = flower_name

        return FLOWERS

def match_letter_to_flower(USER_NAME, FILENAME):
    """Match the first letter of user's name to the flower type"""

    flower_dictionary = create_flower_dictionary(FILENAME)
    first_letter = FIND_FIRST_LETTER_OF_USER_NAME(USER_NAME)

    for letters, flower_names in flower_dictionary.items():
        if first_letter in letters:
            return flower_names

matched_name_to_flower = match_letter_to_flower(USER_NAME, FILENAME)
print(matched_name_to_flower.strip())
