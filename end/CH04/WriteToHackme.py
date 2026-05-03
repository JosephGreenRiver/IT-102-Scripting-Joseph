#!/usr/bin/env python3
# A simple Conditional script in python with Inputs
# Created by Joseph Willoughby 05-02-2026




user_name= input("What is your name?: ")
user_color= input("What is your favorite color?: ")
user_pet= input("What was your first pets name?: ")
user_mother= input("What is your mother's maiden names?: ")
user_elementary= input("What elementary school did you attend?: ")



with open("hackme.txt", "w") as file:
    file.write(f"Name: {user_name}\n")
    file.write(f"Favorite Color: {user_color}\n")
    file.write(f"First Pets Name: {user_pet}\n")
    file.write(f"Mother's Maiden Name: {user_mother}\n")
    file.write(f"Elementary School: {user_elementary}\n")

print("Saved to hackme.txt")
file.close()



