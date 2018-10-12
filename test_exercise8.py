#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise8 import calculate_pizza_slices_per_person, determine_leftover_pizza_slices

class PizzaSliceTest(unittest.TestCase):
    """Tests to calculate the pizza slices per person and any leftover slices"""

    def test_pizza_calculation_per_person(self):
        """How many pizza slices does each person get?"""

        people = 8
        total_pizza_slices = 16
        pizza_slices = calculate_pizza_slices_per_person(people, total_pizza_slices)
        self.assertEqual(pizza_slices, 2)

    def test_leftovers(self):
        """Are there leftover pizza slices?"""

        people = 8
        total_pizza_slices = 16
        leftovers = determine_leftover_pizza_slices(people, total_pizza_slices)
        self.assertEqual(leftovers, 0)

if __name__ == '__main__':
    unittest.main()
    