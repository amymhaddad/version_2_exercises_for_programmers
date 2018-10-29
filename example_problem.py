#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def tip_calculator(bill_amount, tip_rate):
    """Determine the tip for a bill"""

    tip_as_decimal = tip_rate / 100
    total_tip_amount = bill_amount * tip_as_decimal

    return total_tip_amount

def calculate_total_bill(bill_amount, tip):
    """"Calculate the total bill with tip"""

    return bill_amount + tip
