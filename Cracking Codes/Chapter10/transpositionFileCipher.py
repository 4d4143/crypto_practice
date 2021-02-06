# Transposition Cipher Encrypt/Decrypt File
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import time
import os
import sys
import transpositionEncrypt
import transpositionDecrypt


def main():
    inputFilename = 'ejemplo.txt'

    outputFilename = inputFilename[:-4] + '.encrypted.txt'
    myKey = 2
    myMode = 'encrypt'  # Set to encrypt or decrypt

    if not os.path.exists(inputFilename.strip()):
        print('The file %s does not exist...Exiting' % (inputFilename))
        sys.exit()

    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %
        (outputFilename))

        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)

    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__ == '__main__':
    main()
