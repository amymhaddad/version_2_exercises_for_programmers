#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from example_problem import tip_calculator, calculate_total_bill

class TipTestCase(unittest.TestCase):
    """Test for calculating tips at restaurants"""

    def test_tip_calculator(self):
        """Test to see if calculator returns the correct value"""

        bill = 100
        tip_rate = 20
        total_tip = tip_calculator(bill, tip_rate)
        self.assertEqual(total_tip, 20)

    def test_bill_with_tip(self):
        """"Test to calculate the total bill, with tip"""

        bill = 100
        tip = 20
        total_bill = calculate_total_bill(bill, tip)
        self.assertEqual(total_bill, 120)

if __name__ == '__main__':
    unittest.main()
    
