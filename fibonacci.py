n=int(input("Enter the series number:"))
i=1
print("0")
print("1")
a=0
b=1
while(i<=n):
    temp=a+b
    print(temp)
    a=b
    b=temp
    i=i+1