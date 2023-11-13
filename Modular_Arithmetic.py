# Calculate GCD of two numbers
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

# Modular Arithmetic Functions:

# Modular Addition
def mod_add(a, b, m):
    """Modular addition - Add a and b modulo m"""
    return (a + b) % m

# Modular Subtraction  
def mod_sub(a, b, m):
    """Modular subtraction - Subtract b from a modulo m"""
    return (a - b) % m  

# Modular Multiplication
def mod_mul(a, b, m):
    """Modular multiplication - Multiply a and b modulo m"""
    return (a * b) % m

# Modular Multiplicative Inverse
def mod_inv(b, m):
    """Modular multiplicative inverse of b modulo m"""
    g = gcd(b, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return pow(b, m - 2, m)

# Modular Division
def mod_div(a, b, m):
    """Modular division - Divide a by b modulo m"""
    return (a * mod_inv(b, m)) % m

# Usage examples:
a = int(input("Enter a: ")) 
b = int(input("Enter b: "))
m = int(input("Enter m: "))

print(mod_add(a, b, m))
print(mod_sub(a, b, m)) 
print(mod_mul(a, b, m))
print(mod_div(a, b, m))