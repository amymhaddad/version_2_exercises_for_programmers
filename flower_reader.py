#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

FILENAME = 'flowers.txt'
user_name = input('Enter your first and last name: ')
find_first_letters_of_user_name = lambda user_name: user_name[0].title()

def create_flower_dictionary(file_name):
    """Read in a file and create a dictionary"""

    flowers = {}

    with open(file_name) as f_object:
        contents = f_object.readlines()
        for flower in contents:
            split_flower_content = flower.split(" ", 1)
            letter = split_flower_content[0]
            flower_name = split_flower_content[1]
            flowers[letter] = flower_name

        return flowers

def match_letter_to_flower(user_name, file_name):
    """Match the first letter of user's name to the flower type"""

    flower_dictionary = create_flower_dictionary(file_name)
    first_letter = find_first_letters_of_user_name(user_name)

    for letters, flower_names in flower_dictionary.items():
        if first_letter in letters:
            return flower_names

matched_name_to_flower = match_letter_to_flower(user_name, FILENAME)
print(matched_name_to_flower.strip())

