#!/usr/bin/python3

from binascii import unhexlify
import sys
import base64


def convertInputb64(stringInput):
    try:
        byte_seq = unhexlify(stringInput)
        return base64.b64encode(byte_seq)
    except ValueError:
        print("Invalid character! Out of hex character range.")
        sys.exit(1)


if __name__ == '__main__':
    try:
        shellInput = sys.argv[1]
        print(convertInputb64(shellInput))
    except IndexError:
        print("No input was provided! Please provided a hex value.")
        sys.exit(1)
