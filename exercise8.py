#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""
# should my arguments be different than my input variables?
def calculate_pizza_slices_per_person(people, total_slices):
    """Calculate the number of pizza slices each person gets"""

    slices_per_person = total_slices // people
    return slices_per_person

def determine_leftover_pizza_slices(people, total_slices):
    """Determine if there are leftover slices of pizza"""

    leftover_pizza_slices = total_slices % people
    return leftover_pizza_slices
