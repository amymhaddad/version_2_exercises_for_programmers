#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from iteration2_exercise24 import(
    get_two_strings,
    strings_contain_only_letters,
    equal_string_length,
    strings_contain_same_letters,
)

def main():
    """Determine if two strings are anagrams"""

    user_string_1, user_string_2 = get_two_strings()

    only_letters = strings_contain_only_letters(user_string_1, user_string_2)
    strings_are_equal_lengths = equal_string_length(user_string_1, user_string_2)
    strings_with_same_letters = strings_contain_same_letters(user_string_1, user_string_2)

    if only_letters and strings_are_equal_lengths and strings_with_same_letters:
        print(f"{user_string_1.title()} and {user_string_2} are anagrams.")
    else:
        print(f"{user_string_1.title()} and {user_string_2} are not anagrams.")

main()
