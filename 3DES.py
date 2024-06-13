from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Generate a random 24-byte (192-bit) key
key = get_random_bytes(24)

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
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def decrypt(encrypted_text):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    unpadded_text = unpad(decrypted_text)
    return unpadded_text


message = input("Enter message to encrypt: ").encode("utf-8")

encrypted = encrypt(message)
print("Encrypted:", encrypted.hex())

decrypted = decrypt(encrypted)
print("Decrypted:", decrypted.decode("utf-8"))
