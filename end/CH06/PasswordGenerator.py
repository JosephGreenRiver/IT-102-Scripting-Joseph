#!/usr/bin/env python3
# A Simple Password Generator With Choices And Inputs 
# Created by Joseph Willoughby 05-16-2026

"""
This is a basic password generator that will ask the user numerous questions such as
Password Length, To use Uppercase or Lowercase, Digits, Punctuation
"""

#Imported libaries
import string
import secrets

# Define Password Length.
def get_password_length():
    """
    Asks the user for an integer for the password length but has a static minumim set to 8.  
    """
    while True:
      try:
# max() is used to override any integer given that is <8.
        password_length = max(8, int(input("!!Minimum Password Length Is Set To 8!! \nEnter Password Length: ")))
        return password_length
      except ValueError:
           print("That is not a valid integer.")

# Define Users String Choices.
def get_user_choices():
    """
    Asks the user multiple questions to determine the type of the password they want to generate.
    Uppercase, Lowercase, Digits and Punctuation.
    """
# Create a blank list.
    criteria = []
# Asks the user to use both upper and lowercase; if no is selected it will then ask the user to select Uppper or Lower with y/n.
    include_upperlower = input("Uppercase & Lowercase for this password? (y/n): ").strip().casefold()
    if include_upperlower in ("yes", "y"):
        print("Uppercase & Lowercase Will Be Used.\n")
        criteria.append(string.ascii_uppercase)
        criteria.append(string.ascii_lowercase)
    else:
        include_uppercase = input("Uppercase for this password? (y/n): ").strip().casefold()
        if include_uppercase in ("yes", "y"):
            print("Uppercase Will Be Used.\n")
            criteria.append(string.ascii_uppercase)
        else:
            include_lowercase = input("Lowercase for this password? (y/n): ").strip().casefold()
            if include_lowercase in ("yes", "y"):
              print("Lowercase Will Be Used.\n")
              criteria.append(string.ascii_lowercase)

# Choice for including Digits 0-9.
    include_digits = input("Digits for this password 0-9? (y/n): ").strip().casefold()
    if include_digits in ("yes", "y"):
        print("Digits Will Be Used.\n")
        criteria.append(string.digits)

# Choice for including Punctuation.
    include_punctuation = input("Punctuation for this password? (y/n): ").strip().casefold()
    if include_punctuation in ("yes", "y"):
        print("Punctuation Will Be Used.\n")
        criteria.append(string.punctuation)
# Return saves the additons to the list to be used later.
    return criteria

# Define Generate Password to use the users inputed choices.
def generate_password(length, criteria):
    """
    Sets the variables for generating the password and error catching if the user only selects no.
    and ensures at least one charcter frome each catagory selected is used.
    """
    if not criteria:
        return "Error: No options were selected. Cannot generate password."
# Blank list to hold the characters
    password_characters = []
# Ensures that one character is used from each category selected.
    for category in criteria:
        password_characters.append(secrets.choice(category))  
# Put all categories into one pool to fill the password.
    pool = "".join(criteria)
# Determine how many characters are left to generate and fill them.
    remaining_length = length - len(password_characters)
    for _ in range(remaining_length):
        password_characters.append(secrets.choice(pool))    
# Shuffle the list
    secure_rng = secrets.SystemRandom()
    secure_rng.shuffle(password_characters)
# Put the list back into a single string
    return ''.join(password_characters)


# Define Main
def main():
    print("Simple Password Generator")
    print("-------------------------")
# Set variables to the defined functions in the script.
    while True:
        password_length = get_password_length()
        user_choices = get_user_choices()

    # Generates the password and prints the result
        print("Your Password is: \n")
        print(generate_password(password_length, user_choices))

    # Ask the user if they want to generate another password.
        generate_again = input("\nGenerate another password? (y/n): ").strip().casefold()
        if generate_again not in ("yes", "y"):
                print("\nExiting\n")
                # stop the loop and end the script.
                break
            
        print("\nRestarting Password Generator...\n")


if __name__ == "__main__":
    main()