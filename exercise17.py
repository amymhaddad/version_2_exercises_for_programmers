#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

STANDARD_NUMBER_1 = 5.14
MALE_ALCOHOL_DISTRIBUTION_RATIO = 0.73
FEMALE_ALCOHOL_DISTRIBUTION_RATIO = 0.66
STANDARD_NUMBER_2 = 0.15

def calculate_male_bac(alcohol_in_ounces, body_weight, hours):
    """Create a calculate that calculates BAC for males"""

    bac_male = (alcohol_in_ounces * STANDARD_NUMBER_1 / body_weight\
                * MALE_ALCOHOL_DISTRIBUTION_RATIO) - STANDARD_NUMBER_2 * hours

    return bac_male

def calculate_female_bac(alcohol_in_ounces, body_weight, hours):
    """Create a calculate that calculates BAC for females"""

    bac_female = (alcohol_in_ounces * STANDARD_NUMBER_1 / body_weight\
                 * FEMALE_ALCOHOL_DISTRIBUTION_RATIO) - STANDARD_NUMBER_2 * hours

    return bac_female
