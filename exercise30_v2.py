#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

LIST_OF_NUMBERS = list(range(0, 11))

def create_multiplication_table(numbers):
    """Create a table with numbers and product"""

    total_products = []
    for number in numbers:
        for digit in LIST_OF_NUMBERS:
            product = number * digit
            total = f"{number} * {digit} = {product}"
            total_products.append(total)

    return total_products
