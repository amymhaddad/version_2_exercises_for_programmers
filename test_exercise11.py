#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise_11 import convert_currency

class TestCurrencyConversion(unittest.TestCase):
    """Test to convert currencies"""

    def test_calculate_conversion(self):
        """Test to convert euros to dollars"""

        us_exchange_rate = 1.2
        amount_money_in_euros = 55
        euro_exchange_rate = 1.33
        convert_euros_to_dollars = convert_currency\
        (us_exchange_rate, amount_money_in_euros, euro_exchange_rate)
        self.assertEqual(convert_euros_to_dollars, 60.95833333333334)

if __name__ == '__main__':
    unittest.main()
