s=input("Enter a string: ")
vowels="aeiousAEIOUS"
count=0
for ch in s:
    if ch in vowels:
        count+=1
print("Number of vowels: ",count)