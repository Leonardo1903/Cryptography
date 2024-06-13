import hashlib

# Function to perform repeated hashing using a single hash function
def repeated_hash(input_string, num_iterations):
    result = input_string
    for _ in range(num_iterations):
        sha256 = hashlib.sha256()
        sha256.update(result.encode('utf-8'))
        result = sha256.hexdigest()
    return result

# Example usage
input_string = input("Enter a string to hash: ")
num_iterations = int(input("Enter number of iterations: ")) # Number of repeated hash iterations

hashed_string = repeated_hash(input_string, num_iterations)
print(f"Original String: {input_string}")
print(f"{num_iterations}-Time Repeated Hash: {hashed_string}")
