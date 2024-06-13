from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Generate a random 8-byte key and IV
key = get_random_bytes(8)
iv = get_random_bytes(8)

def pad(text):
    # Add padding to make the input a multiple of 8 bytes
    pad_length = 8 - (len(text) % 8)
    padded_text = text + bytes([pad_length] * pad_length)
    return padded_text

def unpad(text):
    # Remove padding
    pad_length = text[-1]
    return text[:-pad_length]

def encrypt(plain_text):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_text = pad(plain_text)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def decrypt(encrypted_text):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(encrypted_text)
    unpadded_text = unpad(decrypted_text)
    return unpadded_text

message = input("Enter message to encrypt: ").encode("utf-8")

encrypted = encrypt(message)
print("Encrypted:", encrypted.hex())

decrypted = decrypt(encrypted)
print("Decrypted:", decrypted.decode("utf-8"))
