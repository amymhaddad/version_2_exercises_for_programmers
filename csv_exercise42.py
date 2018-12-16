#!/usr/bin/env python3
"""
# -*- coding: utf-8 -*-
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import csv

filename = 'employee_data.txt'

employees = [fields for fields in csv.reader(open(filename, newline=''))]

list_of_employees = sorted(employees[1:])
header_line = ''

header_values = employees[0]
string_of_header_values = "\t".join(header_values)
dashes_under_header = '-'*(len(header_values))

employee_data = ''
for employee in list_of_employees:
    employee_lastname = employee[0]
    employee_firstname = employee[1]
    employee_salary = employee[2]

    employee_data += employee_lastname + ' ' + employee_firstname + ' ' + employee_salary + '\n'

final_format = f"{string_of_header_values}\n{dashes_under_header}\n{employee_data}"
