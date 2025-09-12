check=lambda n:"Even"if n % 2==0 else "Odd"
n=int(input("Enter a number: "))
result=check(n)
print(f"{n} is a {result} number")