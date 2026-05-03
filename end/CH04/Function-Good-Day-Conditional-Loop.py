#!/usr/bin/env python3
# A Conditional script with a loop in python with inputs 
# Created by Joseph Willoughby 05-02-2026

# Prompts the user for a y/n answer into a variable
user_answer = input("Is today a good day? (y/n)").casefold()

"""
Loops Yeah it is; if the response is = to y/Y
"""
def send_message():
    for x in range(10):
        print("Yeah it is")

# If the user answers with y/Y it will print "Yes it is" 10 times
if user_answer == "y":
    send_message()

# ElseIf for the user answering with n/N
elif user_answer == "n":
    print("I'm sorry.")
# Else for any other input from the user
else:
    print("Please try again.")