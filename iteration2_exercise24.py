#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import re

def get_two_strings():
    """Get input from user for two strings, and normalize them"""

    user_string_1 = input("Enter one string: ")
    user_string_2 = input("Enter a second string: ")

    return user_string_1.lower(), user_string_2.lower()

def strings_contain_only_letters(user_string_1, user_string_2):
    """Determine if strings contain only letters"""

    string_1_all_letters = re.search(r'^[a-z]+$', user_string_1)
    string_2_all_letters = re.search(r'^[a-z]+$', user_string_2)

    return string_1_all_letters and string_2_all_letters

def equal_string_length(user_string_1, user_string_2):
    """Determine if both strings are the same length"""

    length_string_1 = len(user_string_1)
    length_string_2 = len(user_string_2)

    return length_string_1 == length_string_2

def strings_contain_same_letters(user_string_1, user_string_2):
    """Sort the strings to see if they contain the same letters"""

    sorted_user_string_1 = sorted(user_string_1)
    sorted_user_string_2 = sorted(user_string_2)

    return sorted_user_string_1 == sorted_user_string_2
