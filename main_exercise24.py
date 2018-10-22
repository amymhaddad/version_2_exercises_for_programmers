#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise24 import is_anagram

def main():
    """Get inputs and test if inputs are anagrams"""

    # get inputs
    message = "Enter two words when prompted "
    message += "and I'll tell you if they're anagrams."
    print(message)

    word_1 = input("Enter one word: ")
    word_2 = input("Enter a second word: ")

    # call function
    anagram_tester = is_anagram(word_1, word_2)

    # coordinate output
    if anagram_tester:
        print(f"{word_1.title()} and {word_2} are anagrams.")
    else:
        print("These words aren't anagrams.")

main()
