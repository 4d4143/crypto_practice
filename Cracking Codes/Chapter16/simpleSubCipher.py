#  Simple Substitution Cipher
#  https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import sys
import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    myMessage = """If a man is offered a fact which goes against his
instincts, he will scrutinize it closely, and unless the evidence
is overwhelming, he will refuse to believe it. If, on the other
hand, he is offered something which affords a reason for acting
in accordance to his instincts, he will accept it even on the
slightest evidence. The origin of myths is explained in this way.
-Bertrand Russell"""

    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt'  # set to encrypt or decrypt

    if not keyIsValid(myKey):
        sys.exit("The provided key is not valid")

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print("Using key {}".format(myKey))
    print("The {}ed message is:".format(myMode))
    print(translated)
    print()


def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.up)
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()

        else:
            translated += symbol
    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
