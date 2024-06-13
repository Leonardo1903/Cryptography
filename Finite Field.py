class FiniteFieldElement:
    def __init__(self, val, mod):
        self.value = val
        self.modulus = mod

        # Ensure value is within the finite field
        if self.value < 0 or self.value >= self.modulus:
            self.value %= self.modulus

    def __add__(self, other):
        return FiniteFieldElement((self.value + other.value) % self.modulus, self.modulus)

    def __sub__(self, other):
        return FiniteFieldElement((self.value - other.value + self.modulus) % self.modulus, self.modulus)

    def __mul__(self, other):
        return FiniteFieldElement((self.value * other.value) % self.modulus, self.modulus)

    def __truediv__(self, other):
        # Division is done by multiplying with the modular inverse
        inverse = self.mod_inverse(other.value, self.modulus)
        if inverse == -1:
            raise RuntimeError("Division by zero")
        return FiniteFieldElement((self.value * inverse) % self.modulus, self.modulus)

    def __str__(self):
        return str(self.value)

    # Extended Euclidean algorithm to find the modular inverse
    @staticmethod
    def mod_inverse(a, m):
        m0 = m
        x0, x1 = 0, 1

        while a > 1:
            q = a // m
            t = m

            m = a % m
            a = t

            t = x0
            x0 = x1 - q * x0
            x1 = t

        if x1 < 0:
            x1 += m0

        if a != 1:
            return -1  # Modular inverse does not exist

        return x1


if __name__ == '__main__':
    modulus = 16  # Size of the finite field (2^4)

    # Define the irreducible polynomial x^4 + x + 1
    irreducible_poly = [1, 1, 0, 0, 1]

    # Print the irreducible polynomial
    print("Irreducible Polynomial: ", end="")
    for i in range(len(irreducible_poly)):
        if irreducible_poly[i] == 1:
            print(f"x^{i}", end="")
            if i != len(irreducible_poly) - 1:
                print(" + ", end="")
    print("\n")

    # Create finite field elements
    a = FiniteFieldElement(5, modulus)
    b = FiniteFieldElement(10, modulus)

    # Perform arithmetic operations
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")