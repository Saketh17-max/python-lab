list = [ ]
n=int(input("Enter size of list: "))
for i in  range(n):
	ele=int(input("Enter the Element: "))
	list.append(ele)
print("The list is: ",list)
max=max(list)
min=min(list)
print("Maximum number is",max)
print("Minimum number is",min)	
