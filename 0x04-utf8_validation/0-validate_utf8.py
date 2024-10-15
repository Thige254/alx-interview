#!/usr/bin/python3
"""
This module provides a function for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a given dataset represents a valid UTF-8 encoding.

    Parameters:
    data (list of int): A list of integers representing the bytes of data.

    Returns:
    bool: True if the data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    number_of_bytes = 0

    # Masks to check the first bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each integer (representing a byte)
    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if number_of_bytes == 0:
            # Determine how many bytes are in the current UTF-8 character
            mask = 1 << 7
            while mask & byte:
                number_of_bytes += 1
                mask = mask >> 1

            # If the byte does not indicate a multi-byte character, continue
            if number_of_bytes == 0:
                continue

            # UTF-8 can be at most 4 bytes long
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            # For the remaining bytes, they must start with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes remaining in the sequence
        number_of_bytes -= 1

    # If all characters were valid, the counter should be 0
    return number_of_bytes == 0
