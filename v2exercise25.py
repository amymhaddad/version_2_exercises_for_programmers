#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import re

password = input("Enter your password: ")

digits = re.search(r'^[\d]+$', password)
letters = re.search(r'^[a-zA-Z]+$', password)
letters_and_numbers = re.search(r'^[\w]+$', password)
letters_numbers_characters = re.search(r'^[\W\w]+$', password)

password_length = len(password)

if password_length < 8:
    if digits:
        print("You've got a very weak password.")
    elif letters:
        print("You've got a weak password.")

if password_length >= 8:
    if letters_and_numbers:
        print("You've got a strong password.")
    elif letters_numbers_characters:
        print("You've got a very strong password.")
