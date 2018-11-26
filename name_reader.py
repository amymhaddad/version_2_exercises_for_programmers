#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

FILENAME = 'names.txt'

with open(FILENAME) as f_object:
    contents = sorted(f_object.readlines())
    total_names = len(contents)

    print(f"There are {total_names} names.\n")

    for name in contents:
        print(name.strip())
