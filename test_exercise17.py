#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise17 import calculate_male_bac, calculate_female_bac

class MaleBacTest(unittest.TestCase):
    """Tests blood alcohol level for males and females"""

    def test_male_bac(self):
        """Calculate male bac"""

        alcohol_amount = 10
        weight = 130
        hours_since_last_drink = 1

        male_bac_calculation = calculate_male_bac(alcohol_amount, weight, hours_since_last_drink)
        self.assertEqual(male_bac_calculation, 0.13863076923076925)

    def test_female_bac(self):
        """Calculate female bac"""

        alcohol_amount = 10
        weight = 130
        hours_since_last_drink = 1

        female_bac_calulcation = calculate_female_bac\
                                (alcohol_amount, weight, hours_since_last_drink)
        self.assertEqual(female_bac_calulcation, 0.11095384615384615)

if __name__ == '__main__':
    unittest.main()
