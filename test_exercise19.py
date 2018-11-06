#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise19 import calculate_bmi

class TestBmi(unittest.TestCase):
    """Test to calculate a person's BMI"""

    def test_bmi_calculatation(self):
        """Calculate a person's BMI using inches and pounds"""

        height = 64
        weight = 128
        
        bmi = calculate_bmi(weight, height)
        
        self.assertEqual(bmi, 21.96875)

if __name__ == '__main__':
    unittest.main()
