#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise30_v2 import create_multiplication_table

class TestMultiplicationTable(unittest.TestCase):
    """Test if function generates a multiplication table"""

    LIST_OF_NUMBERS = list(range(0, 11))

    def test_create_multi_table(self):
        """Create a multiplication table using numbers 0 through 9"""

        total_numbers = list(range(0, 13))
    
        complete_multiplication_table = create_multiplication_table(total_numbers)

        self.assertEqual(complete_multiplication_table, complete_multiplication_table)

if __name__ == '__main__':
    unittest.main()
