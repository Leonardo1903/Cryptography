def generate_encryption_key(prime1, prime2, modulus):
    return (prime1 + prime2) % modulus

def encrypt_message(message, encryption_key, modulus, alphabet):
    encrypted_values = []
    
    for char in message:
        if char.isalpha():
            numerical_value = ord(char.upper()) - ord('A') + 1
            encrypted_value = (numerical_value * encryption_key) % modulus
            encrypted_values.append(encrypted_value)
    
    encrypted_letters = [alphabet[value % 26] for value in encrypted_values]
    encrypted_message = ''.join(encrypted_letters)
    
    return encrypted_message

# Given values
prime1 = int(input("Enter 1st prime number: "))
prime2 = int(input("Enter 2nd prime number: "))
modulus = 1000
encryption_key = generate_encryption_key(prime1, prime2, modulus)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Message to encrypt
message = input("Enter a message to encrypt(Only in capital letters): ")

encrypted_message = encrypt_message(message, encryption_key, modulus, alphabet)
print("Original Message:", message)
print("Encryption Key:", encryption_key)
print("Encrypted Message:", encrypted_message)
