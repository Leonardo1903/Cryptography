def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("The modular inverse does not exist (a and m are not coprime).")
    else:
        return x % m

# Example usage:
a = int(input("Enter a: "))
m = int(input("Enter b: "))
inverse = modular_inverse(a, m)
print(f"The modular inverse of {a} modulo {m} is {inverse}")
