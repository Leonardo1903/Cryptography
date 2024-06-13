import hashlib

# Function to perform hierarchical hashing
def hierarchical_hash(input_string, levels):
    result = input_string
    for i in range(levels):
        sha256 = hashlib.sha256()
        sha256.update(result.encode('utf-8'))
        result = sha256.hexdigest()
    return result

# Example usage
input_string = input("Enter a string to hash: ")
levels = int(input("Enter number of levels: ")) # Number of hierarchical levels

hashed_string = hierarchical_hash(input_string, levels)
print(f"Original String: {input_string}")
print(f"{levels}-Level Hierarchical Hash: {hashed_string}")
