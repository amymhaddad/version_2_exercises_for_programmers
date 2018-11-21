#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise12 import convert_rate_to_decimal, calculate_simple_interest

class TestSimpleInterstCalculator(unittest.TestCase):
    """Tests to calculate simple interest"""

    def test_decimal_conversion(self):
        """Test to covert a percent to a decimal"""

        percent = 4.5
        caluclate_percent_to_decimal = convert_rate_to_decimal(percent)
        self.assertEqual(caluclate_percent_to_decimal, 0.045)

    def test_calculate_simple_interest(self):
        """Test to calculate simple interest"""

        principal = 1500
        interest_rate_percent = 4.5
        years_invested = 4
        simple_interest = calculate_simple_interest\
                        (principal, interest_rate_percent, years_invested)
        self.assertEqual(simple_interest, 1770)

if __name__ == "__main__":
    unittest.main()
