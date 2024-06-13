def caesarEncrypt(plaintext, shift):
    encryptedText = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz!@#$%^&*"
    
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
    alphabet = "abcdefghijklmnopqrstuvwxyz!@#$%^&*"
    
    for i in encryptedText:
        if i.islower():
            shiftedIndex = (alphabet.index(i) - shift) % 26
            decryptedText += alphabet[shiftedIndex]
        elif i.isupper():
            shiftedIndex = (alphabet.index(i.lower()) - shift) % 26
            decryptedText += alphabet[shiftedIndex].upper()
    return decryptedText


plaintext = input("Enter the plaintext: ")
shiftAmount = int(input("Enter the shift amount: "))

encrypted = caesarEncrypt(plaintext, shiftAmount)
decrypted = caesarDecrypt(encrypted, shiftAmount)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
