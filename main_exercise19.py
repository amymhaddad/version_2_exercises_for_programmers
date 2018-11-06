#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise19 import calculate_bmi

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

bmi = calculate_bmi(weight, height)

if bmi >= 18.5 and bmi <= 25:
    print("You're BMI is within normal range.")
elif bmi > 25:
    print("Your BMI is above normal. Please see a doctor.")
else:
    print("Your BMI is below normal. Please see a doctor.")
