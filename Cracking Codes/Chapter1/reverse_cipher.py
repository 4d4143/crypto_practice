#Reverse cipher
#https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = input("Please enter a message to be ciphered> ")
translated = ''

#We start from the last index in the "message" string
#And we start adding chars backwards.
#Don't forget to substract from i as we add.
i = len(message) - 1
while i >= 0:
    translated += message[i]
    i -= 1

print(translated)