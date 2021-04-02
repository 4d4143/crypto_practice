#!/usr/bin/python3

import sys


def convertInputHex(stringInput):
    try:
        hexString = int(stringInput, 16)
        return hexString
    except ValueError:
        print("Invalid character! Out of hex character range.")
        sys.exit(1)


if __name__ == '__main__':
    try:
        test = len(sys.argv[1]) == len(sys.argv[2])
        if test:
            bufferOne = convertInputHex(sys.argv[1])
            bufferTwo = convertInputHex(sys.argv[2])
            print(hex(bufferOne ^ bufferTwo))
        else:
            print("Buffers have different size!")
            sys.exit(0)

    except IndexError:
        print("No input was provided! Please provided two hex values.")
        sys.exit(1)
