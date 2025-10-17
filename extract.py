list = [ ]
n=int(input("Enter size of list: "))
even	=[]
odd=[]
for i in  range(n):
	ele=int(input("Enter the element: "))
	list.append(ele)
	if(ele%2==0):
		even.append(ele)
	else:
		odd.append(ele)
print("The Even numbers are",even)
print("The Odd numbers are",odd)			
