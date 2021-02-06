# Affine Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import sys
import random
import cryptoMath

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345\
67890 !?.'


def main():
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRL
QQQQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"
QQQQ-5!1RQP36ARu"""

    myKey = 2894
    myMode = 'decrypt'

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


def checkKeys(keyA, keyB, mode):
    alphabetLength = len(SYMBOLS) - 1

    if keyA == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1.\
             Please choose a different value.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key B is 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > alphabetLength:
        sys.exit('Key A must be greater than 0 and key B must be between\
            0 and {}'.format(alphabetLength))
    if cryptoMath.gcd(keyA, alphabetLength) != 1:
        sys.exit('Key A ({}) and the symbol set size ({}) are not\
            relatively prime. Choose a different key.'.format(
                keyA,
                alphabetLength))


def encryptMessage(key, message):
    lenSymbols = len(SYMBOLS)
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    cipherText = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypt the symbol
            symbolIndex = SYMBOLS.find(symbol)
            cipherText += SYMBOLS[(symbolIndex * keyA + keyB) % lenSymbols]
        else:
            cipherText += symbol  # just append the symbol
    return cipherText


def decryptMessage(key, message):
    lenSymbols = len(SYMBOLS)
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plainText = ''
    modInverseOfA = cryptoMath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            plainText += SYMBOLS[(symbolIndex - keyB) *
                                 modInverseOfA % lenSymbols]
        else:
            plainText += symbol
    return plainText


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptoMath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


if __name__ == '__main__':
    main()
