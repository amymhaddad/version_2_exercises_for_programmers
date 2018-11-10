#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def convert_currency(us_exchange_rate, amount_money_in_euros, euro_exchange_rate):
    """Find exchange rate from euros to US dollars"""

    return (amount_money_in_euros * euro_exchange_rate) / us_exchange_rate
