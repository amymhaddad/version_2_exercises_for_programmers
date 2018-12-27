#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad

"""

from iteration2_exercise_27 import(
    get_employee_input,
    first_name_length,
    last_name_length,
    empty_first_name_value,
    empty_last_name_value,
    correct_id_format,
    correct_zip_code
)

def main():
    """Determine if employee data is valid"""

    #calling functions
    first_name, last_name, employee_id, zip_code = get_employee_input()
    valid_first_name = first_name_length(first_name)
    valid_last_name = last_name_length(last_name)
    empty_first_name = empty_first_name_value(first_name)
    empty_last_name = empty_last_name_value(last_name)
    employee_id_format = correct_id_format(employee_id)
    valid_zip_code = correct_zip_code(zip_code)

    #creating variables
    valid_data = valid_first_name and employee_id_format and valid_zip_code
    name_is_too_short = len(first_name) < 2 or len(last_name) < 2
    too_short_first_name = not valid_first_name
    too_short_last_name = not valid_last_name
    empty_name_field = empty_first_name or empty_last_name

    #calling output
    if valid_data:
        print("No errors.")

    if empty_name_field:
        if empty_first_name and empty_first_name:
            print("You must enter both your first and last name.")
        elif empty_first_name:
            print("You must enter your first name.")
        elif empty_last_name:
            print("You must enter your last name.")

    if name_is_too_short:
        if too_short_first_name:
            print(f"{first_name} is not a valid first name. It's too short.")
        elif too_short_last_name:
            print(f"{last_name} is not a valid last name. It's too short.")

    if not employee_id_format:
        print("You need to enter a valid employee ID.")

    if not valid_zip_code:
        print("Not a valid zip code.")

main()
