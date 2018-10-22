#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def is_anagram(first_word, second_word):
    """Test if words are anagrams"""

    if len(first_word) == len(second_word):
        sorted_first_word = sorted(first_word)
        sorted_second_word = sorted(second_word)
        return sorted_first_word == sorted_second_word
        #The line above gets turned into T or F, in this case T

#This condtional is a boolean expresion and if you return true or false after a conditional it's a duplication
# for ex:
# if len(first_word) == len(second_word):
    # return True ---ex of duplication

        # if sorted_first_word == sorted_second_word:
        #     return True
        # else:
        #     return False

    return False
