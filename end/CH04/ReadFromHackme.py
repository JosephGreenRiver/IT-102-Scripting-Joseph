#!/usr/bin/env python3
# A simple script in python that writes users inputs to a file
# Created by Joseph Willoughby 05-02-2026
"""
A script for collecting users answers and saves to a file
"""


with open("hackme.txt", "r") as file:
    contents= file.read()

# Prints that the information was saved and closes the file.
print(contents)
print("Saved to hackme.txt")
file.close()