SECRET_MESSAGE = '''qeFIP?eGSeECNNS,
5coOMXXcoPSZIWoQI,
avnl1olyD4l'ylDohww6DhzDjhuDil,
z.GM?.cEQc. 70c.7KcKMKHA9AGFK,
?MFYp2pPJJUpZSIJWpRdpMFY,
ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K
Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA
'''

#Every line has a different key.
#We assume the same alphabet used in the chapter has been used here.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

linesToDecode = SECRET_MESSAGE.split('\n')

#I comment this out so it doesnt spam the terminal each time it runs
#If you want to see the messages being decoded, uncomment the following block
"""for line in linesToDecode:
    for key in range(len(SYMBOLS)):
        translated = ''

        for symbol in line:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex += len(SYMBOLS)
                
                translated += SYMBOLS[translatedIndex]
            
            else:
                translated += symbol

        print('Key #%s: %s' % (key, translated))
"""

#After running the script and seeing the correct answers
#we will store the keys for each line here
KEYS = [34, 44, 7, 32, 45, 11, 1]
translated = ''
keysLength = len(KEYS)
index = 0

while index < keysLength:
    key = KEYS[index]
    for symbol in linesToDecode[index]:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]

        else:
            translated += symbol
    translated += '\n'
    index += 1

print(translated)