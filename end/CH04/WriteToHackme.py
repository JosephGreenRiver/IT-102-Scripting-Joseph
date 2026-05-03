#!/usr/bin/env python3
# A simple script in python that writes users inputs to a file
# Created by Joseph Willoughby 05-02-2026
"""
A script for collecting users answers and saves to a file
"""

# Gather users inforamtion into variables.
user_name= input("What is your name?: ")
user_color= input("What is your favorite color?: ")
user_pet= input("What was your first pets name?: ")
user_mother= input("What is your mother's maiden names?: ")
user_elementary= input("What elementary school did you attend?: ")


# Creates/Opens hackme.txt and writes the varibles to multiple lines.
with open("hackme.txt", "w") as file:
    file.write(f"Name: {user_name}\n")
    file.write(f"Favorite Color: {user_color}\n")
    file.write(f"First Pets Name: {user_pet}\n")
    file.write(f"Mother's Maiden Name: {user_mother}\n")
    file.write(f"Elementary School: {user_elementary}\n")

# Prints that the information was saved to hackme.txt
print("Saved to hackme.txt")