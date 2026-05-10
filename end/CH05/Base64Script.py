#!/usr/bin/env python3
# A Base 64 Encoding & Decoding Script in Python with inputs
# Created by Joseph Willoughby 05-10-2026

"""
This script is to take an input and encode and decode BASE64
"""

#Imported libaries
import base64

#Define encode to BASE64

def encode_to_base64(plaintext: str) -> str:  
    """
Encoding Plaintext to BASE64
We will do the following steps
1: Convert the string using UTF-8
2: Pass the bytes into a function called b64.encode
    3: Resulted bytes and return
"""

    text_as_bytes = plaintext.encode("utf-8")
    encoded_bytes = base64.b64encode(text_as_bytes)
    return encoded_bytes.decode("utf-8")

#Define decode to BASE64

def decode_to_base_64(encoded_text: str) -> str:
    """
1: Takes the BASE64 string back to the original Plaintext
2: Convert BASE64 string to get the original bytes
3: Decode those bytes back to utf-8 string
    """
    encoded_as_bytes = encoded_text.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_as_bytes)


#Define main

def main():
    print("Base64 Encoder / Decoder")
    print(" THIS IS NOT ENCRYPTION! ")
    #User inputs
    message = input("Enter your message to encode: ").strip()
    if not message:
        print("No message entered. Exiting")
        return

#Encode
    encoded = encode_to_base64(message)
    print(f"Base64 : {encoded}")

#Decode
    decoded = decode_to_base_64(encoded)

#Validation
    match = decoded == message
    print("Confermation Matched")
    print()

if __name__ == "__main__":
    main()