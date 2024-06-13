def playfairMatrix(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [['' for _ in range(5)] for _ in range(5)]

    i, j = 0, 0
    for letter in key:
        matrix[i][j] = letter
        alphabet = alphabet.replace(letter, "")
        j += 1
        if j == 5:
            i += 1
            j = 0

    for letter in alphabet:
        matrix[i][j] = letter
        j += 1
        if j == 5:
            i += 1
            j = 0
    return matrix

def position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def playfairEncrypt(plain_text, key):
    matrix = playfairMatrix(key)
    plain_text = plain_text.replace(" ", "").upper()
    encrypted_text = ""


    i = 0
    while i < len(plain_text):
        if i == len(plain_text) - 1 or plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[:i + 1] + 'Z' + plain_text[i + 1:]
        i += 2


    i = 0
    while i < len(plain_text):
        letter1 = plain_text[i]
        letter2 = plain_text[i + 1]
        row1, col1 = position(matrix, letter1)
        row2, col2 = position(matrix, letter2)
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        i += 2
    return encrypted_text

def playfairDecrypt(encrypted_text, key):
    matrix = playfairMatrix(key)
    decrypted_text = ""

    i = 0
    while i < len(encrypted_text):
        letter1 = encrypted_text[i]
        letter2 = encrypted_text[i + 1]
        row1, col1 = position(matrix, letter1)
        row2, col2 = position(matrix, letter2)
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        i += 2
    return decrypted_text


key = "Hypnotized"
plain_text = input("Enter plain text: ")
encrypted_text = playfairEncrypt(plain_text, key)
decrypted_text = playfairDecrypt(encrypted_text, key)

print("Playfair Matrix:")
matrix = playfairMatrix(key)
for row in matrix:
    print(" ".join(row))

print("Original Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)



