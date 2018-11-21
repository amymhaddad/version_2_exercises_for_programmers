#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import unittest
from exercise7 import calculate_room_measurement_feet, convert_feet_to_meters

class RoomCalculationsTest(unittest.TestCase):
    """Calculations to get area of room"""

    FEET_TO_METERS_CONVERSION = 0.09290304

    def test_room_measure_feet(self):
        """Test to get room measurement in feet"""

        length = 15
        width = 20

        room_measure_feet = calculate_room_measurement_feet(length, width)

        self.assertEqual(room_measure_feet, 300.0)

    def test_feet_to_meters(self):
        """Test to convert feet to meters"""

        dimensions = 300

        room_from_feet_to_meters = convert_feet_to_meters(dimensions)

        self.assertEqual(room_from_feet_to_meters, 27.870912)

if __name__ == '__main__':
    unittest.main()
