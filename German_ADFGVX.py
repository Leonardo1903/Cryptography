def find_coordinates(grid, char):
    # Iterate through rows
    for i in range(6):
        # Iterate through columns
        for j in range(6):
            # Check if the current cell contains the character
            if grid[i][j] == char:
                # Return the coordinates as letters 'ADFGVX'
                return 'ADFGVX'[i], 'ADFGVX'[j]

def find_character(grid, coord):
    # Find the character in the grid based on coordinates
    row, col = 'ADFGVX'.index(coord[0]), 'ADFGVX'.index(coord[1])
    return grid[row][col]

def adfgvx_encryption(key, plaintext):
    # Define the 6x6 grid for the ADFGVX cipher
    grid = [
        ['A', 'B', 'C', 'D', 'E', 'F'],
        ['G', 'H', 'I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P', 'Q', 'R'],
        ['S', 'T', 'U', 'V', 'W', 'X'],
        ['Y', 'Z', '0', '1', '2', '3'],
        ['4', '5', '6', '7', '8', '9']
    ]

    # Convert the plaintext to uppercase
    plaintext = plaintext.upper()

    # Find the coordinates for each character in the plaintext
    coordinates = [find_coordinates(grid, char) for char in plaintext]

    # Convert the coordinates to the ADFGVX cipher
    ciphertext = ''.join([''.join(coordinate) for coordinate in coordinates])

    # Transpose the ciphertext using the key
    # Sort the ciphertext characters based on their order in the key
    transposed_ciphertext = ''.join(sorted(ciphertext, key=lambda x: key.index(x) if x in key else len(key)))

    return transposed_ciphertext

def adfgvx_decryption(key, ciphertext):
    # Define the 6x6 grid for the ADFGVX cipher
    grid = [
        ['A', 'B', 'C', 'D', 'E', 'F'],
        ['G', 'H', 'I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P', 'Q', 'R'],
        ['S', 'T', 'U', 'V', 'W', 'X'],
        ['Y', 'Z', '0', '1', '2', '3'],
        ['4', '5', '6', '7', '8', '9']
    ]

    # Reverse the transposition using the key
    # Sort the ciphertext characters based on their order in the key
    transposed_ciphertext = ''.join(sorted(ciphertext, key=lambda x: key.index(x) if x in key else len(key)))

    # Convert the ADFGVX cipher to coordinates
    coordinates = [transposed_ciphertext[i:i+2] for i in range(0, len(transposed_ciphertext), 2)]

    # Find the characters in the grid based on coordinates
    decrypted_text = ''.join([find_character(grid, coord) for coord in coordinates])

    return decrypted_text

# Usage
# Get key and plaintext input from the user
key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

# Encrypt the plaintext using ADFGVX cipher and print the result
ciphertext = adfgvx_encryption(key, plaintext)
print("Encrypted Text:", ciphertext)

# Decrypt the ciphertext using ADFGVX cipher and print the result
decrypted_text = adfgvx_decryption(key, ciphertext)
print("Decrypted Text:", decrypted_text)

