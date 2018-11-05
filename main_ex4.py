#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise_ex4 import mad_lib

def main():
    """Create a mad lib game based on user input"""

    user_noun = input("Enter a noun: ")
    user_verb = input("Enter a verb: ")
    user_adverb = input("Enter an adverb: ")
    user_adjective = input("Enter an adjective: ")

    user_sentence = mad_lib(user_noun, user_verb, user_adverb, user_adjective)

    print(user_sentence)

main()
