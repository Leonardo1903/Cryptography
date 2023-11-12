# Calculate (base^exponent) % modulus efficiently using exponentiation by squaring
def powerMod(base, exponent, modulus):
    result = 1 
    base = base % modulus # Reduce base to be within modulus
    while exponent > 0:
        if exponent % 2 == 1: # If exponent is odd
            result = (result * base) % modulus # Multiply result by base
        exponent = exponent // 2 # Integer divide exponent by 2
        base = (base * base) % modulus # Square the base
    return result

# Test if Fermat's Little Theorem holds for the given inputs  
def fermatLittleTheorem(a, p):
    if powerMod(a, p - 1, p) == 1: # Fermat's Little Theorem condition
        return True  
    return False


a = int(input("Enter an integer 'a': ")) 
p = int(input("Enter a prime number 'p': "))

# Validate inputs 
if p <= 1 or a >= p or a <= 0:
    print("Invalid input.")
elif fermatLittleTheorem(a, p):
    print(f"Fermat's Little Theorem holds for a = {a} and p = {p}.")
else:
    print(f"Fermat's Little Theorem does not hold for a = {a} and p = {p}.")