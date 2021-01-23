#Caesar cipher
#https://www.nostarch.com/crackingcodes/ (BSD Licensed)

#import pyperclip

#Message to encrypt
message = "This is my secret message."

#Key used to encrypt/decrypt
key = 13

mode = 'encrypt' #Set to either 'encrypt' or 'decrypt'

#Alphabet
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#variable to store result
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)

        translated += SYMBOLS[translatedIndex]

    else:
        translated += symbol

print(translated)
#pyperclip.copy(translated)
