#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise13 import calculate_compounded_interest_rate

def main():
    principal_amount = float(input("Enter the starting amount of money:$"))
    total_invested_years = float(input("Enter the number of years to invest money: "))
    interest_rate = float(input("Enter the interst rate as a percent: "))
    periods_per_year_to_compound = int(input("Enter the number of periods per year that your money will be compounded: "))

    total = calculate_compounded_interest_rate(principal_amount, total_invested_years, interest_rate, periods_per_year_to_compound)
    
    total_rounded_to_nearest_penny = "{:.2f}".format(total)
    print(f"${int(principal_amount)} invested at {interest_rate}% for {int(total_invested_years)} years is ${total_rounded_to_nearest_penny}.")

main()
