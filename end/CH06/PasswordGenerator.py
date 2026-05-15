#!/usr/bin/env python3
# A Simple Password Generator With Choices And Inputs 
# Created by Joseph Willoughby 05-14-2026

"""
This is a basic password generator that will ask the user numerous questions such as
Password Length, To user Uppercase or Lowercase, Digits, Punctuation
The user 
"""

#Imported libaries
import string
import secrets

# Define Password Length
def get_password_length():
    """
    Asks the user for an integer for the password length but has a static minumim set to 8.  
    """
    while True:
      try:
        password_length = max(8, int(input("Minimum Password Length Is Set To 8! \nEnter Password Length: ")))
        return password_length
      except ValueError:
           print("That is not a valid integer.")

# Define Users String Choices
def get_user_choices():
    """
    Asks the user multiple questions to determine the type of the password they want to generate.
    Uppercase, Lowercase, Digits and Punctuation.
    """

#Creates a blank variable to use for the users choices
    user_choices = ""

# Asks the user to use both upper and lowercase; if no is selected it will then ask the user to select Uppper or Lower with y/n
    include_upperlower = input("Uppercase & Lowercase for this password? (y/n): ").strip().casefold()
    if include_upperlower in ("yes", "y"):
        print("Uppercase & Lowercase Will Be Used.")
        user_choices += string.ascii_letters
    else:
        include_uppercase = input("Uppercase for this password? (y/n): ").strip().casefold()
        if include_uppercase in ("yes", "y"):
            print("Uppercase Will Be Used.")
            user_choices += string.ascii_uppercase
        else:
            include_lowercase = input("Lowercase for this password? (y/n): ").strip().casefold()
            if include_lowercase in ("yes", "y"):
              print("Lowercase Will Be Used.")
              user_choices += string.ascii_lowercase

# Choice for including Digits 0-9.
    include_digits = input("Digits for this password 0-9? (y/n): ").strip().casefold()
    if include_digits in ("yes", "y"):
        print("Digits Will Be Used.")
        user_choices += string.digits

# Choice for including Punctuation.
    include_punctuation = input("Punctuation for this password? (y/n): ").strip().casefold()
    if include_punctuation in ("yes", "y"):
        print("Punctuation Will Be Used.")
        user_choices += string.punctuation
# Return saves the additons to the varible to be used in main()
    return user_choices

# Define Generate Password to use the users inputed choices
def generate_password(length, user_choices):
    """
    Sets the variables for generating the password and error catching if the user only selects no
    """
    if not user_choices:
        return "Error: No string types were selected. Cannot generate password."
    return ''.join(secrets.choice(user_choices) for _ in range(length))

# Define Main
def main():
    print("Simple Password Generator")
    print("")
# Sets variables to defined functions in the script
    password_length = get_password_length()
    user_choices = get_user_choices()

# Generates the password and prints the result
    print("Your Password is: ")
    print(generate_password(password_length, user_choices))

if __name__ == "__main__":
    main()