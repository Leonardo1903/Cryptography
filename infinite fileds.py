class FiniteFieldElement:
    def __init__(self, coeffs):
        self.coefficients = coeffs
        self.degree = len(coeffs) - 1

    def __add__(self, other):
        result_coeffs = [0] * (max(self.degree, other.degree) + 1)
        for i in range(self.degree + 1):
            result_coeffs[i] ^= self.coefficients[i]
        for i in range(other.degree + 1):
            result_coeffs[i] ^= other.coefficients[i]
        return FiniteFieldElement(result_coeffs)

    def __mul__(self, other):
        result_coeffs = [0] * (self.degree + other.degree + 1)
        for i in range(self.degree + 1):
            for j in range(other.degree + 1):
                result_coeffs[i + j] ^= (self.coefficients[i] & other.coefficients[j])
        return FiniteFieldElement(result_coeffs)

    def print(self):
        for i in range(self.degree, -1, -1):
            if self.coefficients[i]:
                if i < self.degree:
                    print(" + ", end="")
                if i == 0 or self.coefficients[i] != 1:
                    print(self.coefficients[i], end="")
                if i > 0:
                    print(f"x^{i}", end="")
        print()

# Define the irreducible polynomial: x^3 + x + 1
irreducible_coeffs = [1, 1, 0, 1]

irreducible = FiniteFieldElement(irreducible_coeffs)

# Define two elements in the finite field
element1_coeffs = [1, 0, 1]
element2_coeffs = [1, 1, 0, 1]

element1 = FiniteFieldElement(element1_coeffs)
element2 = FiniteFieldElement(element2_coeffs)

# Perform addition and multiplication
sum_element = element1 + element2
product_element = element1 * element2

# Print the results
print("Element 1: ", end="")
element1.print()

print("Element 2: ", end="")
element2.print()

print("Sum: ", end="")
sum_element.print()

print("Product: ", end="")
product_element.print()
