#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise12 import calculate_simple_interest

def main():
    """Calculate the simple interest rate"""

    principal_amount = float(input("Enter the principal amount:$"))
    rate_as_percent = float(input("Enter the rate as a percent: "))
    years = float(input("Enter the number of years the money has been invested. If less than one year, type 1. "))

    interest_amount = calculate_simple_interest(principal_amount, rate_as_percent, years)

    print(f"After {int(years)} years at {rate_as_percent}%, the investment will be worth ${int(interest_amount)}.")

main()
