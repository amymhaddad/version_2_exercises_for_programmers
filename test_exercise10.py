#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise10 import calculate_subtotal_for_three_items, tax_rate_to_decimal, total_tax_for_three_items, calculate_grand_total

TAX_RATE = 5.5

class CreateSelfCheckoutSystemTest(unittest.TestCase):
    """Calculate subtotal, total tax, and grand total for three items"""

    def test_subtotal_three_items(self):
        """Get the subtotal for three items"""

        subtotal_item1 = 15
        subtotal_item2 = 15
        subtotal_item3 = 15

        subtotals_three_items = calculate_subtotal_for_three_items(subtotal_item1, subtotal_item2, subtotal_item3)

        self.assertEqual(subtotals_three_items, 45)

    def test_convert_tax_rate_to_decimal(self):
        """Convert tax rate to a decimal"""

        tax_amount = TAX_RATE

        decimal = tax_rate_to_decimal(tax_amount)

        self.assertEqual(decimal, 0.055)

    def test_calculate_total_tax(self):
        """Find total tax for three items"""

        subtotal = 45
        decimal = 0.055

        total_tax = total_tax_for_three_items(subtotal, decimal)

        self.assertEqual(total_tax, 2.475)

    def test_calculate_grand_total(self):
        """Test to calculate grand total: tax plus subtotal"""

        total_tax = 2.475
        subtotal = 45

        grand_total = calculate_grand_total(total_tax, subtotal)

        self.assertEqual(grand_total, 47.475)

if __name__ == '__main__':
    unittest.main()
