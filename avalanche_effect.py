def xor_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % len(key)]
        result = ord(char) ^ ord(key_char)
        ciphertext += chr(result)
    return ciphertext

def xor_decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % len(key)]
        result = ord(char) ^ ord(key_char)
        decrypted_text += chr(result)
    return decrypted_text

plaintext = input("Enter the plaintext: ")
key = input("Enter the encryption key: ")

encrypted_text = xor_encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = xor_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
