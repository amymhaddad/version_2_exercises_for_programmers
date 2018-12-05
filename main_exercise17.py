#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise17 import calculate_male_bac, calculate_female_bac

BAC_LEGAL_LIMIT = 0.08

def main():
    """See if males and females are legally able to drive based on BAC"""

    gender = input("Enter your gender: male or female. ")
    alcohol_amount = int(input("Enter the number of ounces of alcohol you've consumed: "))
    weight = int(input("Enter your weight: "))
    print("Enter the number of hours since your last drink.")
    hours_since_last_drink = int(input("If it's been less than 1 hour, type \'1\'. "))

    male_bac_calcuation = calculate_male_bac(alcohol_amount, weight, hours_since_last_drink)
    female_bac_calculation = calculate_female_bac(alcohol_amount, weight, hours_since_last_drink)

    if gender == 'male':
        if male_bac_calcuation >= BAC_LEGAL_LIMIT:
            rounded_bac_male = "{:.2f}".format(male_bac_calcuation)
            print(f"Your BAC is {rounded_bac_male}. You're not able to drive.")
        else:
            print(f"Your BAC is {rounded_bac_male}.")
    else:
        if female_bac_calculation >= BAC_LEGAL_LIMIT:
            rounded_bac_female = "{:.2f}".format(female_bac_calculation)
            print(f"Your BAC is {rounded_bac_female}. You're not able to drive.")
        else:
            print(f"Your BAC is {rounded_bac_female}.")

main()
