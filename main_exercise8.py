#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

def main():
TOTAL_PEOPLE = int(input("Enter the total number of people eating pizza: "))
TOTAL_PIZZAS = int(input("Enter the total number of pizza you have: "))
TOTAL_PIZZA_SLICES_PER_PIZZA = int(input("Enter the total number of slices per pizza: "))
TOTAL_PIZZA_SLICES = TOTAL_PIZZAS * TOTAL_PIZZA_SLICES_PER_PIZZA

print(f"Each person gets {TOTAL_PIZZA_SLICES_PER_PERSON} pieces of pizza.")

TOTAL_PIZZA_SLICES_PER_PERSON = calculate_pizza_slices_per_person(TOTAL_PEOPLE, TOTAL_PIZZA_SLICES)
LEFTOVERS = determine_leftover_pizza_slices(TOTAL_PEOPLE, TOTAL_PIZZA_SLICES)

if LEFTOVERS == 0:
    print("There are no more pieces of pizza.")
elif LEFTOVERS == 1:
    print("There's one slice of pizza left.")
else:
    print("There are " + str(LEFTOVERS) + "pieces of pizza leftover.")

main()    
