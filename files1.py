f=open('example.bin', 'wb')
file.write(b'\x00\x01\x02\x03\x04\x05')
f=open('example.bin','rb')
print(f.read())
