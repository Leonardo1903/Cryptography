def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(plaintext, a, b):
    ciphertext = ""
    m = 26  
    
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                encrypted_char = chr(((a * x + b) % m) + ord('a'))
            else:
                x = ord(char) - ord('A')
                encrypted_char = chr(((a * x + b) % m) + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext

def decrypt(ciphertext, a, b):
    plaintext = ""
    m = 26  
    a_inv = mod_inverse(a, m)
    
    if a_inv is None:
        return "The 'a' value is not coprime with 26. Choose another 'a' value."
    
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                decrypted_char = chr(((a_inv * (x - b)) % m) + ord('a'))
            else:
                x = ord(char) - ord('A')
                decrypted_char = chr(((a_inv * (x - b)) % m) + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    
    return plaintext


def main():
    a = int(input("Enter first key: "))
    b = int(input("Enter second key: "))
    plaintext = input("Enter plaintext: ")
    
    ciphertext = encrypt(plaintext, a, b)
    print("Encrypted:", ciphertext)
    
    decrypted_text = decrypt(ciphertext, a, b)
    print("Decrypted text:", decrypted_text)

main()