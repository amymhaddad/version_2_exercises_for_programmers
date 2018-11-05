#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise_ex4 import mad_lib

class TestMadLib(unittest.TestCase):
    """Test to create a mad lib sentence"""

    def test_mad_lib_sentence(self):
        """Create a sentence"""

        noun = 'dog'
        verb = "walks"
        adverb = "very"
        adjective = "fast"
        sentence = mad_lib(noun, verb, adverb, adjective)
        self.assertEqual(sentence, "The dog walks very fast.")

if __name__ == '__main__':
    unittest.main()
