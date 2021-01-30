import math


def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext + '|')


def decryptMessage(key, message):
    messageLength = len(message)
    numOfColumns = int(math.ceil(messageLength / key))
    numOfRows = key

    numOfShadedBoxes = (numOfColumns * numOfRows) - messageLength

    plainText = [''] * numOfColumns
    column = 0
    row = 0

    for symbol in message:
        plainText[column] += symbol
        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and
            row >= numOfRows - numOfShadedBoxes):

            column = 0
            row += 1

    return ''.join(plainText)


if __name__ == '__main__':
    main()
