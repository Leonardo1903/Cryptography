import hashlib

# Function to hash a string using SHA-256
def sha256_hash(input_string):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()

# Example usage
input_string = input("Enter a string to hash: ")
hashed_string = sha256_hash(input_string)
print(f"Original String: {input_string}")
print(f"SHA-256 Hash: {hashed_string}")
