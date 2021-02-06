# https://www.nostarch.com/crackingcodes/ (BSD Licensed)


def main():

    myMessage = 'Hola todo bien?'
    myKey = 5

    cipherText = encryptMessage(myKey, myMessage)

    print(cipherText + '|')


def encryptMessage(key, message):

    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]

            currentIndex += key

    return ''.join(ciphertext)


if __name__ == '__main__':
    main()
