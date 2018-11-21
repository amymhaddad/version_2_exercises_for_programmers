#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def convert_rate_to_decimal(rate_as_percent):
    """Convert the rate into a decimal"""

    return rate_as_percent / 100

def calculate_simple_interest(principal_amount, rate_as_percent, years):
    """Test to calculate simple interest"""

    converted_decimal = convert_rate_to_decimal(rate_as_percent)

    return principal_amount * (1 + converted_decimal * years)
