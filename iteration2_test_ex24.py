#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from iteration2_exercise24 import(
    strings_contain_only_letters,
    equal_string_length,
    strings_contain_same_letters,
)

class AnagramChecker(unittest.TestCase):
    """Tests to see if two strings are anagrams"""

    def test_only_letters(self):
        """Test to see if both strings contain only letters"""

        user_string_1 = 'note'
        user_string_2 = 'tone'

        strings_with_only_letters = strings_contain_only_letters(user_string_1, user_string_2)

        self.assertTrue(strings_with_only_letters, True)

    def test_equal_string_lengths(self):
        """Test to see if strings are equal lengths"""

        string_length_1 = 'note'
        string_length_2 = 'tone'

        string_length = equal_string_length(string_length_1, string_length_2)

        self.assertTrue(string_length, True)

    def test_strings_have_same_letters(self):
        """Test to see if both strings contain the same letters"""

        user_string_1 = 'note'
        user_string_2 = 'tone'

        strings_with_letters = strings_contain_same_letters(user_string_1, user_string_2)

        self.assertTrue(strings_with_letters, True)

if __name__ == '__main__':
    unittest.main()
