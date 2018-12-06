#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import random
count = 0

message = print("Type 'q' to quit the game.")
user_level_choice = int(input("What game level do you want to play: 1, 2, or 3? "))

while True:
    user_guess = int(input("Guess the number: "))

    if user_level_choice == 1:
        random_number_level_1 = random.randrange(0, 10)
        if user_guess < random_number_level_1:
            print("Too low. Try again.")
            count += 1
        elif user_guess > random_number_level_1:
            print("Too high. Try again.")
            count += 1
        else:
            print("You got it!")
            count += 1
            play_again = input("Type \'yes.\' to play again or \'q\' to quit: ")
            if play_again == 'yes':
                replay = int(input("What game level do you want to play: 1, 2, or 3? "))
            else:
                break

  
