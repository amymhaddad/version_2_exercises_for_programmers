#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise10 import (
    get_price_quantity,
    get_subtotal,
    calculate_sum_of_subtotals,
    calculate_total_tax_for_items,
    calculate_grand_total,
)

TAX_RATE = 5.5

def main():
    """Create a self-checkout system that calculates the grand total for three items"""

    price_item1, quantity_item1 = get_price_quantity()
    print("\n")
    price_item2, quantity_item2 = get_price_quantity()
    print("\n")
    price_item3, quantity_item3 = get_price_quantity()

    subtotal_item1 = get_subtotal(price_item1, quantity_item1)
    subtotal_item2 = get_subtotal(price_item2, quantity_item2)
    subtotal_item3 = get_subtotal(price_item3, quantity_item3)

    sum_of_subtotals = calculate_sum_of_subtotals(subtotal_item1, subtotal_item2, subtotal_item3)
    total_tax_for_items = calculate_total_tax_for_items(TAX_RATE, sum_of_subtotals)
    grand_total = calculate_grand_total(total_tax_for_items, sum_of_subtotals)

    formatted_output = f"""
    The grand total is ${grand_total:.2f}.
    The subtotal is ${sum_of_subtotals:.2f}.
    The total tax is ${total_tax_for_items:.2f}.
    """

    print(formatted_output)

main()
