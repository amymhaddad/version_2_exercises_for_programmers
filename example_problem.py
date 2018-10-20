#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def tip_calculator(bill, tip_rate):
    """Determine the tip for a bill"""

    tip_as_decimal = tip_rate / 100
    total_tip_amount = bill * tip_as_decimal

    return total_tip_amount
