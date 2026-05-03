#!/usr/bin/env python3
# A simple script in python that reads from a file and prints the contents
# Created by Joseph Willoughby 05-02-2026
"""
A script to read and print user answers from hackme.txt
"""

# Opens hackme.txt and reads the entire file.
with open("hackme.txt", "r") as file:
    contents= file.read()

# Prints the information that was stored.
print("Here is someone to hack - information")
print(contents)