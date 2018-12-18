#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

calculate_subtotal_for_three_items = lambda subtotal_item1, subtotal_item2, subtotal_item3: subtotal_item1 + subtotal_item2 + subtotal_item3

tax_rate_to_decimal = lambda tax: tax/100

total_tax_for_three_items = lambda subtotals, decimal: subtotals * decimal

calculate_grand_total = lambda total_tax, subtotals: total_tax + subtotals
