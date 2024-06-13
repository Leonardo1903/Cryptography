def gf_mul(a, b):
    result = 0
    while b > 0:
        if b & 1:
            result ^= a
        high_bit_set = a & 0x80
        a <<= 1
        if high_bit_set:
            a ^= 0x1b
        b >>= 1
    return result

def gf_add(a, b):
    return a ^ b

def extended_euclidean(a, b):
    x, y, x1, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y, y1 = y1, y - q * y1
        x, x1 = x1, x - q * x1
    return b, x, y

def gf_inverse(a):
    gcd, x, _ = extended_euclidean(a, 0x1b)
    if gcd != 1:
        return None
    else:
        return x % 256

# Example usage
a = 0x57
b = 0x83
print("GF multiplication:", hex(gf_mul(a, b)))
print("GF addition:", hex(gf_add(a, b)))
