#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise1 import print_greeting

def main():
    """Get input from user and print a greeting"""

    # get input
    user_name = input("What is your name? ")

    # call function
    user_greeting = print_greeting(user_name)

    # coordinate output
    print(user_greeting)

main()
