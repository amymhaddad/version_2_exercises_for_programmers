#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad

"""
import re

def get_employee_input():
    """Get employee information"""

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    employee_id = input("Enter your employee ID: ")
    zip_code = input("Enter your zip code: ")

    return first_name, last_name, employee_id, zip_code


def first_name_length(first_name):
    """See if first name is at least two characters"""

    return re.match(r'[a-zA-Z]{2,50}', first_name)

def last_name_length(last_name):
    """See if last name is at least two characters"""

    return re.match(r'[a-zA-Z]{2,50}', last_name)


def empty_first_name_value(first_name):
    """See if user filled out their last name"""

    return re.match(r'^\s*$', first_name)

def empty_last_name_value(last_name):
    """See if user filled out their last name"""

    return re.match(r'^\s*$', last_name)


def correct_id_format(employee_id):
    """See if employee ID is in the correct format"""

    return re.match(r'[A-Z]{2}-\d{4}', employee_id)


def correct_zip_code(zip_code):
    """See if zip code contains all digits"""

    return re.match(r'[\d]+', zip_code)
