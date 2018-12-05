#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise30_v2 import create_multiplication_table

def main():
    """Input to generate a multiplication table"""

    numbers = list(range(0, 13))
    string_of_totals = ''

    multiplication_table = create_multiplication_table(numbers)

    for total in multiplication_table:
        string_of_totals += total + '\n'
    print(string_of_totals)

main()
