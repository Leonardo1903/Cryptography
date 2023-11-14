# Galois Field class 
class GaloisField:

    def __init__(self, p, irr_poly):
        self.p = p # Prime modulus
        self.irr_poly = irr_poly # Irreducible polynomial
        
    def add(self, a, b):
        return (a + b) % self.p

    def multiply(self, a, b):
        if a == 0 or b == 0:
            return 0 
        r = 0
        while b > 0:
            if b & 1: # Check if b is odd
                r = r ^ a
            b = b >> 1 # Equivalent to b // 2
            a = a << 1 # Equivalent to a * 2
        return r % self.irr_poly
    
    def print_irr_poly(self):
        print(f"Irreducible Polynomial: {self.irr_poly}")

# Get user inputs
p = int(input("Enter prime number p: ")) # 7
irr_poly = int(input("Enter irreducible polynomial: ")) # 11

# Create Galois Field
gf = GaloisField(p, irr_poly)

print("Galois Field Created:")  
gf.print_irr_poly()

# Get elements  
a = int(input("\nEnter element a: ")) # 2
b = int(input("Enter element b: ")) # 3

# Demo field operations
print(f"\na + b = {gf.add(a, b)}")
print(f"a * b = {gf.multiply(a, b)}\n")