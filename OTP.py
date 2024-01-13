import random

def generate_key(message):
  return ''.join(str(random.randint(0, 9)) for _ in range(len(message)))

def encrypt(message, key):
  return ''.join(str((int(m) + int(k)) % 10) for m, k in zip(message, key))

def decrypt(ciphertext, key):
  return ''.join(str((int(c) - int(k)) % 10) for c, k in zip(ciphertext, key))

# Usage
message = input("Enter message: ")
key = generate_key(message)
encrypted = encrypt(message, key)
print("Encrypted: ", encrypted)
decrypted = decrypt(encrypted, key)
print("Decrypted: ", decrypted)
