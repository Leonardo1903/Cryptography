import string

def createVigenereMatrix():
    alphabet = string.ascii_uppercase
    vigenereMatrix = [[' ' for _ in range(26)] for _ in range(26)]
    
    for row in range(26):
        for col in range(26):
            vigenereMatrix[row][col] = alphabet[(row + col) % 26]
    
    return vigenereMatrix

def vigenereEncrypt(plainText, key):
    vigenereMatrix = createVigenereMatrix()
    plainText = plainText.upper()
    key = key.upper()
    encryptedText = ""

    for i in range(len(plainText)):
        if plainText[i] == ' ':
            encryptedText += ' '
        else:
            row = ord(key[i % len(key)]) - ord('A')
            col = ord(plainText[i]) - ord('A')
            encryptedText += vigenereMatrix[row][col]

    return encryptedText

def vigenereDecrypt(encryptedText, key):
    vigenereMatrix = createVigenereMatrix()
    encryptedText = encryptedText.upper()
    key = key.upper()
    decryptedText = ""

    for i in range(len(encryptedText)):
        if encryptedText[i] == ' ':
            decryptedText += ' '
        else:
            row = ord(key[i % len(key)]) - ord('A')
            col = vigenereMatrix[row].index(encryptedText[i])
            decryptedText += chr(col + ord('A'))

    return decryptedText


key = "Hypnotized"
plainText = input("Enter plain text: ")
    
encryptedText = vigenereEncrypt(plainText, key)
decryptedText = vigenereDecrypt(encryptedText, key)
    
print("Vigenère Matrix:")
for row in createVigenereMatrix():
    print(" ".join(row))
    
print("\nPlain Text:   ", plainText)
print("Encrypted Text:", encryptedText)
print("Decrypted Text:", decryptedText)