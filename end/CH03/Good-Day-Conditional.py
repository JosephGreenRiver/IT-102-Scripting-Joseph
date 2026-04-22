#!/usr/bin/env python3
# A simple Conditional script in python with Inputs
# Created by Joseph Willoughby 04-22-2026

# Prompts the user for a y/n answer into a variable
user_answer = input("Is today a good day? (y/n)").casefold()

# If the user answers with y/Y it will print "Yes it is"
if user_answer == "y":
    print("Yes it is!")
elif user_answer == "n":
    print("I'm sorry.")
else:
    print("Please try again.")


#### LOOP ASSIGNEMT
