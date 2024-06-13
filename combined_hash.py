import hashlib

# Function to perform combined hashing using multiple hash functions
def combined_hash(input_string):
    hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]
    combined_result = b""

    for hash_func in hash_functions:
        hasher = hash_func()
        hasher.update(input_string.encode('utf-8'))
        hash_result = hasher.digest()  # Get the binary hash result
        combined_result += hash_result

    # Final combined hash as a hexadecimal string
    combined_hash_hex = combined_result.hex()

    return combined_hash_hex

# Example usage
input_string = input("Enter a string to hash: ")

combined_hash_result = combined_hash(input_string)

print(f"Original String: {input_string}")
print(f"Combined Hash: {combined_hash_result}")
