# Define elliptic curve equation
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
p = input("Enter the value of p: ")

# Define an elliptic curve point
point = (int(input("Enter the value of x: ")), int(input("Enter the value of y: ")))

# Define point addition
def add(p1, p2):
    if p1 is None: 
        return p2
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 != y2:
        return None

    if p1 == p2:
        lam = (3*x1*x1 + a) * pow(2*y1, p-2, p)
    else:
        lam = (y2-y1) * pow(x2-x1, p-2, p)

    x3 = lam*lam - x1 - x2 
    y3 = lam*(x1-x3) - y1
    return (x3 % p, y3 % p)

# Define point doubling  
def double(p):
    x, y = p
    lam = (3*x*x + a) * pow(2*y, p-2, p)
    x3 = lam*lam - 2*x
    y3 = lam*(x-x3) - y 
    return (x3 % p, y3 % p)

# Compute point multiplication
def multiply(p, n):
    r = None
    for i in range(n):
        r = add(r, p)
    return r

# Usage
k = input("Enter the value of k: ")
print(multiply(point, k))