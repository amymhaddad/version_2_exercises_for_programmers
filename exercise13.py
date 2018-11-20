#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def turn_percent_to_decimal(interest_rate):
    """Turn the percent into a decimal"""

    return interest_rate / 100

def calculate_compounded_interest_rate(principal_amount, total_invested_years, interest_rate, periods_per_year_to_compound):
    """Calculate compounded interest rate"""

    decimal = turn_percent_to_decimal(interest_rate)
    compounded_interest_rate = principal_amount * (1 + (decimal / periods_per_year_to_compound) ** (periods_per_year_to_compound * total_invested_years))

    return compounded_interest_rate
