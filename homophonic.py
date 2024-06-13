import random
import string

# Function to generate a random substitution key
def generateSubstitutionKey():
    key = list(string.ascii_uppercase)
    shuffledKey = key[:]
    random.seed()
    random.shuffle(shuffledKey)
    return ''.join(shuffledKey)

# Function to encrypt a message using the homophonic substitution cipher
def encryptHomophonicCipher(message, key):
    ciphertext = ""
    alphabet = string.ascii_uppercase

    # Encrypt the message
    for char in message:
        if char.isalpha():
            uppercaseC = char.upper()
            index = ord(uppercaseC) - ord('A')
            ciphertext += key[index]
        else:
            ciphertext += char  # Keep non-alphabet characters unchanged

    return ciphertext

message = input("Enter a message to encrypt: ")
substitutionKey = generateSubstitutionKey()

print("Original Message:", message)
print("Substitution Key:", substitutionKey)

ciphertext = encryptHomophonicCipher(message, substitutionKey)

print("Encrypted Message:", ciphertext)
