# Define an array that stores the reverse substitution for each character
encryptionKey = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

def findPosition(target):
    for i in range(len(encryptionKey)):
        if encryptionKey[i] == target:
            return i
    return -1  # Character not found

def encrypt(plaintext):
    ciphertext = ""
    for c in plaintext:
        encryptedChar = c
        if c.isalpha():
            if c.islower():
                encryptedChar = encryptionKey[ord(c) - ord('a')]
            else:
                encryptedChar = encryptionKey[ord(c) - ord('A')]
        ciphertext += encryptedChar
    return ciphertext

def decrypt(ciphertext):
    plaintext = ""
    for c in ciphertext:
        decryptedChar = c
        if c.isalpha():
            if c.islower():
                decryptedChar = chr(ord('a') + findPosition(c))
            else:
                decryptedChar = chr(ord('A') + findPosition(c))
        plaintext += decryptedChar
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter a string to encrypt: ")
    encryptedText = encrypt(plaintext)
    decryptedText = decrypt(encryptedText)

    print("Original:", plaintext)
    print("Encrypted:", encryptedText)
    print("Decrypted:", decryptedText)
