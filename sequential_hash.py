import hashlib

# Function to perform sequential hashing
def sequential_hash(input_string, num_iterations):
    result = input_string
    for _ in range(num_iterations):
        sha256 = hashlib.sha256()
        sha256.update(result.encode('utf-8'))
        result = sha256.hexdigest()
    return result

# Example usage
input_string = input("Enter a string to hash: ")
num_iterations = int(input("Enter number of iterations: "))  # Number of sequential hash iterations

hashed_string = sequential_hash(input_string, num_iterations)
print(f"Original String: {input_string}")
print(f"{num_iterations}-Step Sequential Hash: {hashed_string}")
