from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Generate a random 8-byte key and IV
key = get_random_bytes(8)
iv = get_random_bytes(8)

def encrypt(plain_text):
    cipher = DES.new(key, DES.MODE_OFB, iv)
    encrypted_text = cipher.encrypt(plain_text)
    return encrypted_text

def decrypt(encrypted_text):
    cipher = DES.new(key, DES.MODE_OFB, iv)
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text


message = input("Enter message to encrypt: ").encode("utf-8")


encrypted = encrypt(message)
print("Encrypted:", encrypted.hex())

decrypted = decrypt(encrypted)
print("Decrypted:", decrypted.decode("utf-8"))
