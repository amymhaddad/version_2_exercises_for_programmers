#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

BILL_AMOUNT = float(input("What is the bill? "))
TIP_AMOUNT = float(input("What is the tip amount? "))

def tip_calculator(bill, tip_rate):
    """Determine the tip for a bill"""

    bill = float(bill)
    tip_rate = float(tip_rate)

    tip_as_decimal = tip_rate / 100
    total_tip_amount = bill * tip_as_decimal

    return total_tip_amount

TIP = tip_calculator(BILL_AMOUNT, TIP_AMOUNT)

BILL_WITH_TIP = BILL_AMOUNT + TIP
TOTAL_BILL_STATEMENT = (f"The total with tip is ${BILL_WITH_TIP:.2f}.\n")
TOTAL_BILL_STATEMENT += (f"The tip is ${TIP:.2f}.")
print(TOTAL_BILL_STATEMENT)
