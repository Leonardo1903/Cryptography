# Define alphabet to use for encryption/decryption
alphabet = "abcdefghijklmnopqrstuvwxyz!@#$%^&*"

# Caesar encryption function
def caesarEncrypt(plaintext, shift):
    # Encrypted text 
    encryptedText = ""
    # Loop through each character in plaintext
    for char in plaintext:
    # Handle lowercase letters
        if char.islower():
            # Get shifted index in alphabet
            shiftedIndex = (alphabet.index(char) + shift) % 26
            # Add encrypted letter to result
            encryptedText += alphabet[shiftedIndex]
        # Handle uppercase letters  
        elif char.isupper():
            # Get shifted index for lowercase version  
            shiftedIndex = (alphabet.index(char.lower()) + shift) % 26
            # Add encrypted uppercase letter to result
            encryptedText += alphabet[shiftedIndex].upper()
    # Return encrypted text
    return encryptedText


# Caesar decryption function  
def caesarDecrypt(encryptedText, shift):
    # Decrypted text
    decryptedText = ""
    # Loop through encrypted text
    for char in encryptedText:
        # Handle lowercase letters
        if char.islower():
            # Get shifted index in reverse
            shiftedIndex = (alphabet.index(char) - shift) % 26
            # Add decrypted letter to result
            decryptedText += alphabet[shiftedIndex]
        # Handle uppercase letters
        elif char.isupper():
            # Get shifted index in reverse for lowercase version
            shiftedIndex = (alphabet.index(char.lower()) - shift) % 26
            # Add decrypted uppercase letter
            decryptedText += alphabet[shiftedIndex].upper()
    # Return decrypted text
    return decryptedText

# Get plaintext input  
plaintext = input("Enter the plaintext: ")

# Define shift amount
shiftAmount = 3

# Encrypt plaintext
encrypted = caesarEncrypt(plaintext, shiftAmount)

# Decrypt ciphertext 
decrypted = caesarDecrypt(encrypted, shiftAmount)

# Print results
print("Plaintext:", plaintext)
print("Encrypted:", encrypted) 
print("Decrypted:", decrypted)