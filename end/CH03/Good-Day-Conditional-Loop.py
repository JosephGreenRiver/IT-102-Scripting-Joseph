#!/usr/bin/env python3
# A simple Conditional script with a Loop in python with Inputs
# Created by Joseph Willoughby 04-22-2026

# Prompts the user for a y/n answer into a variable
user_answer = input("Is today a good day? (y/n)").casefold()

# If the user answers with y/Y it will print "Yes it is" 10 times
if user_answer == "y":
    for x in range(10):
        print("Yes it is!")
# ElseIf for the user answering with n/N
elif user_answer == "n":
    print("I'm sorry.")
# Else for any other input from the user
else:
    print("Please try again.")