import random

def caesarEncrypt(plaintext, shift):
    encryptedText = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in plaintext:
        if i.islower():
            shiftedIndex = (alphabet.index(i) + shift) % 26
            encryptedText += alphabet[shiftedIndex]
        elif i.isupper():
            shiftedIndex = (alphabet.index(i.lower()) + shift) % 26
            encryptedText += alphabet[shiftedIndex].upper()
    return encryptedText

def caesarDecrypt(encryptedText, shift):
    decryptedText = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in encryptedText:
        if i.islower():
            shiftedIndex = (alphabet.index(i) - shift) % 26
            decryptedText += alphabet[shiftedIndex]
        elif i.isupper():
            shiftedIndex = (alphabet.index(i.lower()) - shift) % 26
            decryptedText += alphabet[shiftedIndex].upper()
    return decryptedText


plaintext = input("Enter the plaintext: ")
randList = [" "]
for i in range(100,999):
    randList.append(i)
# print(randList)
shiftAmount = random.choice(randList)
print("Random key: ", shiftAmount)

encrypted = caesarEncrypt(plaintext, shiftAmount)
decrypted = caesarDecrypt(encrypted, shiftAmount)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
