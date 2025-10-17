f=open('demo.txt', 'w')
f.write('Hello world!')
f.close()
f=open('demo.txt', 'r')
print(f.read())
f.close()
f=open('demo.txt', 'r')
print(f.read(2))
f.close()
f=open('demo.txt', 'r')
print(f.readline())
f.close()
f=open('demo.txt', 'r')
print(f.readlines())
f.close()
#list of Strings
lines=[
	"First line of the file\n",
	"Second line of the file\n",
	"Third line of the file\n"
	]
f=open('example.txt','w')
f.writelines(lines)
f=open('example.txt','r')
print(f.read())
f.close()	
f=open('example.txt','r')
content=f.read(6)
position=f.tell()
print('Current position: ',position)
f=open('example.txt','r')
f.seek(10)
print('Updated position: ',f.tell())

