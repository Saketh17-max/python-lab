import numpy as np
arr=np.array([10,20,30,40,50])
print("Original:",arr)
print("Slicing[1:4]:",arr[1:4])
print("Integer Indexing:",arr[[0,2,4]])
print("Boolean Indexing:",arr[arr>30])

