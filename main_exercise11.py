#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise_11 import convert_currency

def main():
    """Convert euros to dollars"""

    us_exchange_rate = 1.2
    amount_money_in_euros = int(input("Enter the amount of money you have in euros: "))
    euro_exchange_rate = float(input("As a decimal, enter the euro exchange rate: "))

    euros_to_dollars = convert_currency(us_exchange_rate, amount_money_in_euros, euro_exchange_rate)

    print(f"The conversion from euros to dollars is ${ROUNDED_EXCHANGE_RATE(euros_to_dollars)}.")

ROUNDED_EXCHANGE_RATE = lambda currency: (f"{currency:.2f}")

main()
