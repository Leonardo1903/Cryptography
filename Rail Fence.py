def encryptRailFence(plainText, rails):
    railMatrix = [['\n' for _ in range(len(plainText))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0

    for char in plainText:
        if row == 0 or row == rails - 1:
            direction *= -1

        railMatrix[row][col] = char
        col += 1
        row += direction

    encryptedText = ''.join([char for row in railMatrix for char in row if char != '\n'])
    return encryptedText, railMatrix

def decryptRailFence(encryptedText, rails):
    railMatrix = [['\n' for _ in range(len(encryptedText))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0

    for i in range(len(encryptedText)):
        if row == 0 or row == rails - 1:
            direction *= -1

        railMatrix[row][col] = '*'
        col += 1
        row += direction

    index = 0
    for row in range(rails):
        for col in range(len(encryptedText)):
            if railMatrix[row][col] == '*' and index < len(encryptedText):
                railMatrix[row][col] = encryptedText[index]
                index += 1

    direction = -1
    row, col = 0, 0
    decryptedText = ""

    for i in range(len(encryptedText)):
        if row == 0 or row == rails - 1:
            direction *= -1

        if railMatrix[row][col] != '\n':
            decryptedText += railMatrix[row][col]
            col += 1
            row += direction

    return decryptedText

text = input("Enter plain text: ")
rails = 5

encryptedText, railMatrix = encryptRailFence(text, rails)
print("Encrypted:", encryptedText)

print("Rail Matrix:")
for row in railMatrix:
    print(' '.join([char if char != '\n' else '-' for char in row]))

decryptedText = decryptRailFence(encryptedText, rails)
print("Decrypted:", decryptedText)