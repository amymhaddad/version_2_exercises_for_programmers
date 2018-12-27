#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad

"""

import unittest
from iteration2_exercise_27 import(
    first_name_length,
    last_name_length,
    empty_first_name_value,
    empty_last_name_value,
    correct_id_format,
    correct_zip_code
)

class VerifyEmployeeData(unittest.TestCase):
    """Tests to verify valid employee data"""

    def test_valid_first_name(self):
        """Test if first name is valid, meaning it's at least two characters long"""

        first_name = 'Amy'

        verify_first_name = first_name_length(first_name)

        self.assertTrue(verify_first_name, True)

    def test_valid_last_name(self):
        """Test if last name is valid, meaning it's at least two characters long"""

        last_name = 'Haddad'

        verify_last_name = last_name_length(last_name)

        self.assertTrue(verify_last_name, True)

    def test_empty_first_name_value(self):
        """Test if the first name value is empty"""

        first_name = ' '

        empty_first_name = empty_first_name_value(first_name)

        self.assertTrue(empty_first_name, True)

    def test_empty_last_name_value(self):
        """Test if the last name value is empty"""

        last_name = "Haddad"

        empty_last_name = empty_last_name_value(last_name)

        self.assertFalse(empty_last_name, False)

    def test_id_format(self):
        """Test if employee id is in the correct format"""

        employee_id = 'AA-1234'

        employee_id_format = correct_id_format(employee_id)

        self.assertTrue(employee_id_format, True)

    def test_correct_zip_code(self):
        """Test to see if zip code contains all digits"""

        zip_code = '12345'

        employee_zip_code_contents = correct_zip_code(zip_code)

        self.assertTrue(employee_zip_code_contents, True)

if __name__ == '__main__':
    unittest.main()
