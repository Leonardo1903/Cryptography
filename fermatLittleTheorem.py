def powerMod(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 20
        base = (base * base) % modulus
    return result

def fermatLittleTheoremTest(a, p):
    if powerMod(a, p - 1, p) == 1:
        return True
    return False


a = int(input("Enter an integer 'a': "))
p = int(input("Enter a prime number 'p': "))

if p <= 1 or a >= p or a <= 0:
    print("Invalid input.")
elif fermatLittleTheoremTest(a, p):
    print(f"Fermat's Little Theorem holds for a = {a} and p = {p}.")
else:
    print(f"Fermat's Little Theorem does not hold for a = {a} and p = {p}.")
