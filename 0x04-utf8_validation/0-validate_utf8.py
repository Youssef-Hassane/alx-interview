#!/usr/bin/python3
"""
The minimum operations coding challenge.
"""

def validUTF8(data):
    """
      Args:
          data (list): list of integers
      Returns:
          int: number of bytes consumed by the data
    """
    def is_valid_byte(byte, num_bytes):
        # Check if the byte follows the pattern based on the number of bytes expected
        if num_bytes == 1:
            return (byte & 0b10000000) == 0
        elif num_bytes == 2:
            return (byte & 0b11000000) == 0b10000000
        elif num_bytes == 3:
            return (byte & 0b11100000) == 0b11100000 and (byte & 0b00100000) == 0
        elif num_bytes == 4:
            return (byte & 0b11110000) == 0b11110000 and (byte & 0b00001000) == 0
        return False

    num_bytes = 0
    for byte in data:
        if not (0 <= byte <= 255):
            return False

        if num_bytes == 0:
            if (byte & 0b10000000) == 0b00000000:
                continue
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            if not is_valid_byte(byte, num_bytes):
                return False
            num_bytes -= 1

    return num_bytes == 0
