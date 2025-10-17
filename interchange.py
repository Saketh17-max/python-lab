list = [ ]
n=int(input("Enter size of list: "))
for i in  range(n):
	ele=int(input("Enter the Element: "))
	list.append(ele)
print("The given list is :",list)
list.insert(0,100)
list.insert(n-1,200)
print("The updated list is:",list)
