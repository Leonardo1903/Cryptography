def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    
    numColumns = len(key)
    
    numRows = (len(plaintext) + numColumns - 1) // numColumns
    padding = numRows * numColumns - len(plaintext)
    plaintext += "Z" * padding
    
    matrix = [['' for _ in range(numColumns)] for _ in range(numRows)]
    
    index = 0
    for col in range(numColumns):
        for row in range(numRows):
            matrix[row][col] = plaintext[index]
            index += 1
    
    ciphertext = ''
    for col in key:
        col_index = int(col) - 1
        for row in range(numRows):
            ciphertext += matrix[row][col_index]
    print(matrix)
    
    return ciphertext

def decrypt(ciphertext, key):
    numColumns = len(key)
    
    numRows = len(ciphertext) // numColumns
    
    matrix = [['' for _ in range(numColumns)] for _ in range(numRows)]
    
    index = 0
    for col in key:
        col_index = int(col) - 1
        for row in range(numRows):
            matrix[row][col_index] = ciphertext[index]
            index += 1
    
    plaintext = ''
    for row in range(numRows):
        for col in range(numColumns):
            plaintext += matrix[row][col]
    
    return plaintext


plaintext = input("Enter plaintext: ")
key = "2413"  # Example key
print("Plaintext: ", plaintext)
print("Key: ", key)

ciphertext = encrypt(plaintext, key)
print("Encrypted: ", ciphertext)

decryptedText = decrypt(ciphertext, key)
print("Decrypted: ", decryptedText)


