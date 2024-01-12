def homophonic_encryption(key, plaintext):
   # Convert the plaintext to uppercase
   plaintext = plaintext.upper()

   # Encrypt the plaintext
   ciphertext = ''.join([key[char] for char in plaintext])

   return ciphertext

def homophonic_decryption(key, ciphertext):
   # Create a reverse key
   reverse_key = {v: k for k, v in key.items()}

   # Decrypt the ciphertext
   plaintext = ''.join([reverse_key[char] for char in ciphertext])

   return plaintext

# Define the key for the Homophonic Substitution Cipher
key = {
   'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
   'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0',
   'K': '!', 'L': '@', 'M': '#', 'N': '$', 'O': '%',
   'P': '^', 'Q': '&', 'R': '*', 'S': '(', 'T': ')',
   'U': '-', 'V': '+', 'W': '=', 'X': '[', 'Y': ']',
   'Z': '{', ' ': ' '
}


# Get plaintext input from the user
plaintext = input("Enter plaintext: ")

# Encrypt the plaintext using Homophonic Substitution Cipher and print the result
ciphertext = homophonic_encryption(key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext using Homophonic Substitution Cipher and print the result
decrypted_plaintext = homophonic_decryption(key, ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
