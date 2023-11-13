# Extended Euclidean Algorithm to find gcd and coefficients x, y 
# that satisfy ax + by = gcd(a, b)

def extended_euclidean(a, b):
    # Initialize s, old_s, t, old_t to keep track of coefficients
    s = 0; old_s = 1
    t = 1; old_t = 0
    # Initialize r to b and old_r to a
    r = b; old_r = a
    while r != 0:
        # Update quotients and coefficients in each step
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s 
        old_t, t = t, old_t - quotient * t
    # Once r becomes 0, old_r is gcd and old_s, old_t are coefficients
    return old_r, old_s, old_t

a = int(input("Enter a: "))
b = int(input("Enter b: "))

gcd, x, y = extended_euclidean(a, b)

print(gcd)
print(x, y)