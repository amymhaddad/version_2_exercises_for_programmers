#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise32 import random_int_level_1, response_to_user_guess_too_high, response_to_user_guess_too_low, response_to_user_guess_correct

import random
count = 0

message = print("Type 'q' to quit the game.")
user_level_choice = int(input("What game level do you want to play: 1, 2, or 3? "))

while True:
    user_guess = int(input("Guess the number: "))
    user_guess_too_high = response_to_user_guess_too_high(user_guess)
    user_guess_too_low = response_to_user_guess_too_low(user_guess)
    user_correct_guess = response_to_user_guess_too_high(user_guess)

    if user_level_choice == 1:
        if user_guess_too_high:
            print("Your guess is too high. Try again.")
            count += 1
        elif user_guess_too_low:
            print("Your guess is too low. Try again")
            count += 1
        else:
            print("You got it!")
            count += 1
            play_again = input("Type \'yes.\' to play again or \'q\' to quit: ")
            if play_again == 'yes':
                replay = int(input("What game level do you want to play: 1, 2, or 3? "))
            else:
                break




#Original that works
# while True:
#     user_guess = int(input("Guess the number: "))

#     if user_level_choice == 1:
#         random_number_level_1 = random.randrange(0, 10)
#         if user_guess < random_number_level_1:
#             print("Too low. Try again.")
#             count += 1
#         elif user_guess > random_number_level_1:
#             print("Too high. Try again.")
#             count += 1
#         else:
#             print("You got it!")
#             count += 1
#             play_again = input("Type \'yes.\' to play again or \'q\' to quit: ")
#             if play_again == 'yes':
#                 replay = int(input("What game level do you want to play: 1, 2, or 3? "))
#             else:
#                 break
