def find_coordinates(grid, char):
    # Iterate through rows
    for i in range(6):
        # Iterate through columns
        for j in range(6):
            # Check if the current cell contains the character
            if grid[i][j] == char:
                # Return the coordinates as letters 'ADFGVX'
                return 'ADFGVX'[i], 'ADFGVX'[j]

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

# Usage
# Get key and plaintext input from the user
key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

# Encrypt the plaintext using ADFGVX cipher and print the result
print(adfgvx_encryption(key, plaintext))
