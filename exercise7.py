#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

FEET_TO_METERS_CONVERSION = 0.09290304

def calculate_room_measurement_feet(length, width):
    """Calculate the size of a room in feet"""

    area = length * width
    return area

def convert_feet_to_meters(dimensions):
    """Convert the dimensions from feet to meters"""

    square_meters = float(dimensions) * FEET_TO_METERS_CONVERSION
    return square_meters
