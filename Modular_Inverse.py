# Extended Euclidean algorithm to find gcd and coefficients of Bezout's identity
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Find modular inverse using extended Euclidean algorithm
def modular_inverse(a, m):
    
    # Call extended gcd to get gcd and coefficients of Bezout's identity
    gcd, x, y = extended_gcd(a, m)
    
    # Raise error if gcd is not 1, modular inverse does not exist
    if gcd != 1:
        raise ValueError("The modular inverse does not exist (a and m are not coprime).")
    
    # Return x mod m as the modular inverse        
    else:
        return x % m

# Example usage:
a = int(input("Enter a: ")) 
m = int(input("Enter b: "))

# Call modular_inverse function        
inverse = modular_inverse(a, m)
print(f"The modular inverse of {a} modulo {m} is {inverse}")