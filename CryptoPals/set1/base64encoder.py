from bitarray import bitarray
from bitarray.util import ba2int

base64mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcd\
efghijklmnopqrstuvwxyz0123456789+/"

testString1 = "49276d206b696c6c696e6720796f757220627261696e206c\
696b65206120706f69736f6e6f7573206d757368726f6f6d"

stringBits = bitarray()
# We create an unitialized bitarray
stringBits.frombytes(testString1.encode('utf-8'))
# We convert the string to bits

b64stringList = []  # To store the corresponding b64 chars

for sequence in range(0, len(stringBits), 6):
    # We scan the bitarray 6 bits at a time
    b64stringList += base64mapping[(ba2int(stringBits[sequence:sequence+6]))]
    # We store the corresponding b64 char into b64stringlist
    
print(len(stringBits) % 6)
# Lets see the result
