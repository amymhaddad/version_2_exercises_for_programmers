#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

from exercise7 import calculate_room_measurement_feet, convert_feet_to_meters

def main():
    """Get room dimensions and calcuate measurements in square feet and square meters"""

    FEET_TO_METERS_CONVERSION = 0.09290304

    # get inputs and print a statement
    room_length = float(input("Enter the length of the room in feet: "))
    room_width = float(input("Enter the width of the room in feet: "))

    print(f"You entered dimensions of {room_length} by {room_width}.")

    # call functions
    room_size_feet = calculate_room_measurement_feet(room_length, room_width)
    room_size_square_meters = convert_feet_to_meters(room_size_feet, FEET_TO_METERS_CONVERSION)

    # coordinate and customize output
    print(f"The area is {int(room_size_feet)} square feet and {room_size_square_meters:.3f} square meters.")

main()
