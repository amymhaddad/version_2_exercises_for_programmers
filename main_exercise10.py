#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise10 import calculate_subtotal_for_three_items, tax_rate_to_decimal, total_tax_for_three_items, calculate_grand_total

TAX_RATE = 5.5

def main():
    """Find the subtotal, tax, and grand total for three items"""

    #Get input from user
    price_item1 = int(input("Enter the price of item 1: "))
    quantity_item1 = int(input("Enter the quantity of item 1: "))
    subtotal_item1 = price_item1 * quantity_item1
    print('\n')

    price_item2 = int(input("Enter the price of item 2: "))
    quantity_item2 = int(input("Enter the quantity of item 2: "))
    subtotal_item2 = price_item2 * quantity_item2
    print('\n')

    price_item3 = int(input("Enter the price of item 3: "))
    quantity_item3 = int(input("Enter the quantity of item 3: "))
    subtotal_item3 = price_item3 * quantity_item3
    print('\n')

    #Make calcuations: subtotal, total tax, and grand total for three items
    subtotals = calculate_subtotal_for_three_items(subtotal_item1, subtotal_item2, subtotal_item3)
    decimal = tax_rate_to_decimal(TAX_RATE)
    total_tax = total_tax_for_three_items(subtotals, decimal)
    grand_total = calculate_grand_total(total_tax, subtotals)

    #Coordinate output
    subtotal_output = f"The subtotal is ${subtotals:.2f}."
    total_tax_amount = f"The total tax is ${total_tax:.2f}."
    subtotal_and_tax = f"The grand total is ${grand_total:.2f}."

    print(subtotal_output)
    print(total_tax_amount)
    print(subtotal_and_tax)

main()
