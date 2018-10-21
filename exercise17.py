#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def calculate_male_bac(alcohol_in_ounces, body_weight, hours):
    """Create a calculate that calculates BAC for males"""

    bac_male = (alcohol_in_ounces * 5.14 / body_weight * 0.73) - .015 * hours

    return bac_male

def calculate_female_bac(alcohol_in_ounces, body_weight, hours):
    """Create a calculate that calculates BAC for females"""

    bac_female = (alcohol_in_ounces * 5.14 / body_weight * 0.66) - .015 * hours

    return bac_female
