#!/usr/bin/env python3
'''
/************************/
/*    mod_enc_dec.py    */
/*     Version 1.0      */
/*     2024/03/14       */
/************************/
'''
import json
import numpy as np
import os
import sys


def load_charmap():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    charmap_path = os.path.join(dir_path, 'charmap.json')
    with open(charmap_path) as json_file:
        data = json.load(json_file)
    return (
        data['hp48_enc']['charmap_0_63'] +
        data['charmap_64_127'] +
        data['charmap_128_191'] +
        data['charmap_192_255']
    )


def decode(string: str, isFile: bool = False) -> str:
    if isFile:
        with open(string, 'r') as file:
            string = file.read()

    # Strip all spaces and line feeds
    string = string.replace(" ", "").replace("\n", "")

    # Check if the string starts with "ENC", followed by a number,
    # "T", and is at least 14 characters long
    if len(string) < 14 or not (string.startswith("ENC") and
                                string[3].isdigit() and string[4] == "T"):
        raise ValueError(
            "The string must start with 'ENC', '\
            'followed by a number, 'T', and be at least 14 characters long.")

    # Extract the next 5 characters after "ENC[number]T",
    # convert to number, subtract 10000
    checksum_str = string[5:10]
    try:
        checksum = int(checksum_str) - 10000
    except ValueError:
        raise ValueError(
            "The next 5 characters after 'ENC[number]T' should be a number.")

    # Check that the 11th character is "S"
    if string[10] != "S":
        raise ValueError("The 11th character must be 'S'.")

    # Strip the first 11 characters
    string = string[11:]

    # Check if the length of encoded_string is a multiple of 3
    if len(string) % 3 != 0:
        raise ValueError(
            "The length of the encoded string must be a multiple of 3.")

    charmap_v = np.array(load_charmap())
    decoded_string = ""
    for i in range(0, len(string), 3):
        # Extract the current 3-character block
        block = string[i:i + 3]

        # Convert the block to a number and Adjust it
        num = int(block) - 100
        checksum -= num  # Adjust checksum

        # Map the number to a character using charmap_v
        try:
            decoded_char = charmap_v[num]
            decoded_string += decoded_char
        except ValueError:
            raise ValueError(
                f"Number {num} is out of range for the character map.")

    if checksum != 0:
        raise ValueError("Checksum validation failed.")
    return (decoded_string)


def encode(string: str, isFile: bool = False, enc_type: int = 3) -> str:
    if isFile:
        with open(string, 'r') as file:
            string = file.read()
    # Proceed with encoding
    if string.startswith("%%HP"):
        string = '\n'.join(string.splitlines()[1:])
    string = string.strip()
    charmap_dict = {v: k for k, v in enumerate(load_charmap()) if v}
    # start from 10000 to ensure 5 digits
    checksum = 10000
    encoded_string = ""
    i = 0
    while i < len(string):
        sequence = ""
        if string[i] == "\\":
            # Check if the next character is also a backslash
            if i + 1 < len(string) and string[i + 1] == "\\":
                # It's a double backslash, treat it as a single character
                sequence = "\\\\"
                i += 2  # Skip the next backslash
            else:
                # It's a single backslash,
                # look ahead for the end of the sequence
                sequence += string[i]
                i += 1
                # case like "\<<T" are NOT handled, spaces are needed
                while i < len(string) and string[i] \
                        not in [" ", "\n", "\t", "\r", "\\"]:
                    sequence += string[i]
                    i += 1
        else:
            # No backslash, just a regular character
            sequence = string[i]
            i += 1  # Move to the next character

        # Encode the sequence or character
        try:
            char_value = charmap_dict[sequence]
        except ValueError:
            raise ValueError(f"Unmapped sequence or character: '{sequence}'")

        checksum += char_value
        # add 100 to ensure 3 digits
        encoded_value = char_value + 100
        encoded_string += f"{encoded_value}"

    encoded_string = "ENC"+ str(enc_type) + "T" + str(checksum) + "S" +\
        encoded_string
    return encoded_string


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise 'Must be using Python 3'
    pass
