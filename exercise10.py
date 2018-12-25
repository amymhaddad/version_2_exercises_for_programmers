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


def calculate_sum_of_subtotals(subtotal_item1, subtotal_item2, subtotal_item3):
    """Add all subtotals together to get sum of subtotals"""

    return subtotal_item1 + subtotal_item2 + subtotal_item3


def convert_tax_to_decimal(TAX_RATE):
    """Convert given tax rate to a decimal"""

    return TAX_RATE / 100


def calculate_total_tax_for_items(TAX_RATE, sum_of_subtotals):
    """Calculate the total tax: tax rate as decimal * sum of the subtotals"""

    tax_rate_as_decimal = convert_tax_to_decimal(TAX_RATE)

    return tax_rate_as_decimal * sum_of_subtotals


def calculate_grand_total(total_tax_for_items, sum_of_subtotals):
    """Find grand total: tax plus sum of subtotals for items"""

    return total_tax_for_items + sum_of_subtotals
