#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import random

def random_int_level_1():
    """Generate a random number for level 1"""

    return random.randrange(0, 10)

def response_to_user_guess_too_high(user_guess):
    """Return a print statement that notifies user that their guess is too high"""

#it's calling the random number again
    random_number_level_1 = random_int_level_1()
    guess_too_high = user_guess > random_number_level_1
    
    return guess_too_high

def response_to_user_guess_too_low(user_guess):
    """Return a print statement that notifies user that their guess is too low"""

    random_number_level_1 = random_int_level_1()
    guess_too_low = user_guess < random_number_level_1

    return guess_too_low

def response_to_user_guess_correct(user_guess):
    """Return a print statement if user guess is correct"""

    random_number_level_1 = random_int_level_1()
    correct_guess = user_guess == random_number_level_1

    return correct_guess
