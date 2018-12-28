#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def get_price_quantity():
    """Get price and quantity from user"""

    price = float(input("Enter the price:$"))
    quantity = int(input("Enter the quantity: "))

    return price, quantity


def get_subtotal(price, quantity):
    """Calculate subtotal: price * quantity"""

    return price * quantity


def sum_of_subtotals(*subtotals):
    """Add all subtotals together to get sum of subtotals"""

    totals = [subtotal for subtotal in subtotals]

    return sum(totals)


def convert_tax_to_decimal(tax_rate):
    """Convert given tax rate to a decimal"""

    return tax_rate / 100


def total_tax_for_multiple_items(tax_rate_as_decimal, subtotals_sum):
    """Calculate the total tax: tax rate as decimal * sum of the subtotals"""

    return tax_rate_as_decimal * subtotals_sum


def grand_total(total_tax_multiple_items, subtotals_sum):
    """Find grand total: tax plus sum of subtotals for items"""

    return total_tax_multiple_items + subtotals_sum
