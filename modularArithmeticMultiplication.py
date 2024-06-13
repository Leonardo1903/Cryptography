
def modularMultiplication(a,b,c) :
    if (((a*b)%c)==((a%c)*(b%c))%c):
        return True
    else:
        return False

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of c: "))

if (modularMultiplication(a,b,c)):
    print("Modular multiplication is valid for these numbers")
else:
    print("Modular multiplication is not valid for these numbers")