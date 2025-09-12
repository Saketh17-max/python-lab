def fibonacci(n):
    if n<=1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter a number: "))
result=fibonacci(n)
print(f"The fabonacci of {n} is {result}")