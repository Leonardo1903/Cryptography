def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def eulerTotientFunction(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count = count + 1
    return count

n = int(input("Enter a positive integer n: "))
result = eulerTotientFunction(n)
print(f"The value of Euler's Totient Function phi({n}) is {result}")
