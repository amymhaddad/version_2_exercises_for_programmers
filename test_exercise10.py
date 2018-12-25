#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise10 import (
    get_subtotal,
    calculate_sum_of_subtotals,
    convert_tax_to_decimal,
    calculate_total_tax_for_items,
    calculate_grand_total,
)

class SelfCheckoutTest(unittest.TestCase):
    """Test to see if self-checkout system calculates grand total for three items"""

    def test_subtotal(self):
        """Test to calculate subtotal"""

        price = 5.0
        quantity = 3

        calculate_subtotal = get_subtotal(price, quantity)

        self.assertEqual(calculate_subtotal, 15.0)

    def test_calculate_subtotals_sum(self):
        """Test to add all of the subtotals together"""

        subtotal_1 = 10
        subtotal_2 = 10
        subtotal_3 = 10

        subtotal_sum = calculate_sum_of_subtotals(subtotal_1, subtotal_2, subtotal_3)

        self.assertEqual(subtotal_sum, 30)

    def test_convert_tax_rate_to_decimal(self):
        """Test to convert given tax rate to decimal"""

        tax_rate = 5.5

        rate_to_decimal_conversion = convert_tax_to_decimal(tax_rate)

        self.assertEqual(rate_to_decimal_conversion, 0.055)

    def test_calculate_total_tax(self):
        """Test to calculate total tax for items"""

        tax_rate = 5.5
        sum_of_subtotals = 30

        total_tax = calculate_total_tax_for_items(tax_rate, sum_of_subtotals)

        self.assertEqual(total_tax, 1.65)

    def test_calucate_grand_total(self):
        """Test calucation for grand total, tax plus subtotal"""

        total_tax = 1.65
        sum_subtotals = 30

        grand_total = calculate_grand_total(total_tax, sum_subtotals)

        self.assertEqual(grand_total, 31.65)

if __name__ == '__main__':
    unittest.main() 
