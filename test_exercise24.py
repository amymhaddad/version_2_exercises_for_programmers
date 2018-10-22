#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise24 import is_anagram

class AnagramTestCase(unittest.TestCase):
    """Anagram test"""

    def test_two_words(self):
        """Test to see if two words are anagrams"""

        word_1 = 'note'
        word_2 = 'tone'
        anagram_test = is_anagram(word_1, word_2)
        self.assertEqual(anagram_test, True)

if __name__ == '__main__':
    unittest.main()
    