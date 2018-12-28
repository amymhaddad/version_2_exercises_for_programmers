#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise10 import (
    get_price_quantity,
    get_subtotal,
    sum_of_subtotals,
    convert_tax_to_decimal,
    total_tax_for_multiple_items,
    grand_total,
)

TAX_RATE = 5.5

def main():
    """Create a self-checkout system that calculates the grand total for three items"""

    price_item1, quantity_item1 = get_price_quantity()
    print()
    price_item2, quantity_item2 = get_price_quantity()
    print()
    price_item3, quantity_item3 = get_price_quantity()

    subtotal_item1 = get_subtotal(price_item1, quantity_item1)
    subtotal_item2 = get_subtotal(price_item2, quantity_item2)
    subtotal_item3 = get_subtotal(price_item3, quantity_item3)

    total_subtotals = sum_of_subtotals(subtotal_item1, subtotal_item2, subtotal_item3)
    tax_rate_as_decimal = convert_tax_to_decimal(TAX_RATE)
    total_tax = total_tax_for_multiple_items(tax_rate_as_decimal, total_subtotals)
    subtotal_and_tax = grand_total(total_subtotals, total_tax)

    formatted_output = f"""
    The grand total is ${subtotal_and_tax:.2f}.
    The subtotal is ${total_subtotals:.2f}.
    The total tax is ${total_tax:.2f}.
    """

    print(formatted_output)

main()

