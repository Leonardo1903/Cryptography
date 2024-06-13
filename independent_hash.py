import hashlib

# Function to perform independent hashing using multiple hash functions
def independent_hash(input_string):
    hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]
    results = []

    for hash_func in hash_functions:
        hasher = hash_func()
        hasher.update(input_string.encode('utf-8'))
        hash_result = hasher.hexdigest()
        results.append(hash_result)

    return results

# Example usage
input_string = input("Enter a string to hash: ")

hash_results = independent_hash(input_string)

print(f"Original String: {input_string}")
for i, result in enumerate(hash_results):
    print(f"Hash function {i + 1}: {result}")
