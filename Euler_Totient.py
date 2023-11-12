# Function to calculate GCD of two numbers
def gcd(a, b):
    while b != 0: 
        a, b = b, a % b
    return a

# Function to calculate Euler's Totient function
def eulerTotientFunction(n):
    # Initialize counter 
    count = 0
    # Loop from 1 to n
    for i in range(1, n + 1):
        # If gcd(n, i) is 1
        if gcd(n, i) == 1:
            # Increment counter 
            count = count + 1
            
    return count

# Take input from user  
n = int(input("Enter a positive integer n: "))
# Call eulerTotientFunction()
result = eulerTotientFunction(n)
# Print result
print(f"The value of Euler's Totient Function phi({n}) is {result}")
