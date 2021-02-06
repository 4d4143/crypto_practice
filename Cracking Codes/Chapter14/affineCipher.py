# Affine Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import sys
import random
import cryptoMath

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345\
67890 !?.'


def main():
    myMessage = """"A computer would deserve to be called intelligent
    if it could deceive a human into believing that it was human."
    -Alan Turing"""

    myKey = 2894
    myMode = 'encrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('Key: {}'.format(myKey))
    print('{}ed text'.format(myMode.title()))
    print(translated)


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)

    return (keyA, keyB)


def checkKeys():


def encryptMessage():


def decryptMessage():


def getRandomKey():


if __name__ == '__main__':
    main()
