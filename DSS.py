def mod_exp(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod

        exp = exp >> 1
        base = (base * base) % mod

    return result


# Step 1: Generate DSA Parameters
p = 257
q = 13
g = 2

# Step 2: Generate Private and Public Keys
x = 6  # Private key
y = mod_exp(g, x, p)  # Public key

# Step 3: Sign a Message
k = 7  # Random number
r = mod_exp(g, k, p) % q
Hm = 123  # Replace with actual hash of the message
s = (k * (Hm + x * r)) % q

# Step 4: Verify the Signature
w = 1  # s^(-1) mod q (Assuming s is relatively prime to q)
u1 = (Hm * w) % q
u2 = (r * w) % q
v = (mod_exp(g, u1, p) * mod_exp(y, u2, p)) % p % q

if v == r:
    print("Signature is valid.")
else:
    print("Signature is invalid.")