def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
result=gcd(a,b)
print(f"The Gcd of {a} and {b} is {result}")