list = [ ]
n=int(input("Enter size of list: "))
for i in  range(n):
	ele=int(input("Enter the Element: "))
	list.append(ele)
sum=sum(list)	
avg=sum/ n	
print("sum is: ",sum)
print("average is: ",avg)
