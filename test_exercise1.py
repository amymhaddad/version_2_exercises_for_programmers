#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise1 import generate_greeting

class GreetUserTest(unittest.TestCase):
    """Test greeting"""

    def test_greeting(self):
        """Test if greeting returns user's name with a greeting"""

        name = "amy"
        display_greeting = generate_greeting(name)
        self.assertEqual(display_greeting, "Hello, Amy. It's nice to meet you!")

if __name__ == '__main__':
    unittest.main()
