#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from example_problem import tip_calculator, calculate_total_bill

def main():
    """Calculate tip and total bill with tip"""

# inputs for function
    bill_amount = float(input("What is the bill? "))
    tip_percent = float(input("What is the tip percent? "))

# call function with variables
    tip_calculation = tip_calculator(bill_amount, tip_percent)
    bill_with_tip = calculate_total_bill(bill_amount, tip_calculation)

# customize output
    total_bill_statement = (f"The total with tip is ${bill_with_tip:.2f}.\n")
    total_bill_statement += (f"The tip is ${tip_calculation:.2f}.")
    print(total_bill_statement)

main()
