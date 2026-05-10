#!/usr/bin/env python3
# A basic Caesar cipher encryption and decryption program in python with inputs 
# Created by Joseph Willoughby 05-09-2026

"""
This is a basic Caesar cipher encryption and decryption program 
that will take the users inputed message and encrypt it by the users selected shift value
the user can choose to decrypt their message and recive a validation that the decryption was sucessfull
"""



#Define Encrypt
def cesar_encrypt(message: str, shift:int) -> str:
    """
    Encrypts a message by shfiting each letter a "shift" amount.
    A-Z
    a-z

    """
    result = []

    for char in message:
        if char.isupper():    
                shifted = (ord(char) - ord("A") + shift) % 26 + ord("A")
                result.append(chr(shifted))
        elif char.islower():
                shifted = (ord(char) - ord("a") + shift) % 26 + ord("a") 
                result.append(chr(shifted))
        else: 
            result.append(char)
    return "".join(result)

#Define Decrypt
def ceasar_decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypt a Caesar Cipher message by shifing the letters backwards.
    """

    return cesar_encrypt(ciphertext, -shift)

#Define Shift Value
def get_shift_value() -> int:
    """
    Promts the user for the amount of shifts to take.
    """

    while True:
            try:
                shift = int(input("Enter a value between 1-25: "))
                if 1 <= shift <= 25:
                    return shift
                print("Please enter a valid shift")
            except ValueError:
                print("That is noit a valid integer.")


#Define Main
def main ():
    print("Ceasar Cipher Encrypt and Decrypt")
    message = input("Enter a message: ").strip()
    if not message:
         print("Noo message entered. Exiting")
         return

    #get the shift value
    shift = get_shift_value()

    #Encrypt
    encrypted = cesar_encrypt(message, shift)
    print(F"Encrypted Message: {encrypted}")

    #Decrypted if user 
    answer = input("Decrypt the message? (yes/no): ").strip().casefold()

    if answer in ("yes", "y"):
         decrypted = ceasar_decrypt(encrypted, shift)
         print(F"Decrypted Message: {decrypted}")

        #confirm
         match = decrypted == message
         print("Validation of match")
    else:
        print("Decryption skipped")
    print()

if __name__ == "__main__":
    main()