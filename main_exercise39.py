#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise39 import sort_employees

def main():
    """Format employee details"""

    xiong = {
        'first_name': 'tou',
        'last_name': 'xiong',
        'position': 'software engineer',
        'separation_date': '2016-10-05',
    }

    johnson = {
        'first_name': 'john',
        'last_name': 'johnson',
        'position': 'manager',
        'separation_date': '2016-12-31',
    }

    michaelson = {
        'first_name': 'michaela',
        'last_name': 'michaelson',
        'position': 'district manager',
        'separation_date': '2015-12-19',
    }

    jacobson = {
        'first_name': 'jake',
        'last_name': 'jacobson',
        'position': 'programmer',
        'separation_date': ' ',
    }

    jackson = {
        'first_name': 'jacquelyn',
        'last_name': 'jackson',
        'position': 'dba',
        'separation_date': ' ',
    }

    weber = {
        'first_name': 'sally',
        'last_name': 'weber',
        'position': 'web developer',
        'separation_date': '2015-12-18',
    }

    employees = [xiong, johnson, michaelson, jacobson, jackson, weber]
    list_of_employees = ['xiong', 'johnson', 'michaelson', 'jacobson', 'jackson', 'weber']

    sorted_employees_in_alpha_order = sort_employees(list_of_employees)

    for sorted_employee_lastname in sorted_employees_in_alpha_order:
    # inner loop; loop through the dictionaries
        for employee in employees:
        # get a match: match "sorted_employee_lastname" from outerloop with "employee['last_name']" from inner loop so I can extract info
            if sorted_employee_lastname == employee['last_name']:
                if employee['position'] == 'dba':
                    position_title = employee['position'].upper()
                else:
                    position_title = employee['position'].title()
                full_name = employee['first_name'].title() + ' ' + employee['last_name'].title()
                date_separation = employee['separation_date']

                employee_info = full_name + ' | ' + position_title + ' | ' + date_separation
                print(employee_info)

main()
