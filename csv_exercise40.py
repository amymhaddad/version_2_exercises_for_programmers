#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import csv

imported_data = [fields for fields in csv.reader(open("data_exercise40.txt", newline =''))]

user_search = input("Enter your search: ")
normalized_user_search = user_search.title()

total_employee_data = [details for details in imported_data]

header_row = total_employee_data[0]
del header_row[0:2]
header_row.insert(0, "Fullname")
string_of_headers = ' | '.join(header_row) 
row_of_dashes = "-"*len(string_of_headers)

employee_data = ''

for employees in total_employee_data[1:]:
        full_name_format = ' '.join(employees[:2]) 
        position_format = employees[2]
        separation_date_format = employees[3]

        if normalized_user_search in full_name_format:
                employee_data += full_name_format + ' | ' + position_format + ' | ' + separation_date_format + '\n'

final_format = f"{string_of_headers}\n{row_of_dashes}\n{employee_data}"

print(final_format)
