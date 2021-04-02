#!/usr/bin/python3
import binascii

xoredString = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

for argument in range(ord("A"), ord("z")):
    result = xoredString ^ argument
    print()
