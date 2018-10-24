#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise39 import sort_employees

class EmployeeDetailsTest(unittest.TestCase):
    """Test to see sort employee last names"""

    def test_sort_employee_lastnames(self):
        """Return last names in alphabetical order?"""

        employee_lastnames = ['xiong', 'johnson', 'michaelson', 'jacobson', 'jackson', 'weber']
        alpha_order_employee_lastnames = sort_employees(employee_lastnames)
        self.assertEqual(alpha_order_employee_lastnames, ['jackson', 'jacobson', 'johnson', 'michaelson', 'weber', 'xiong'])

if __name__ == '__main__':
    unittest.main()
    