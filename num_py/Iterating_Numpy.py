_author_ = "aman"
import numpy as np

narr = np.arange(0,6)
print(narr)

print("*" * 40 , "iterating through one dimensional array")
for item in narr:
    print(item)

print("*" * 40 , "iterating through one dimensional array with index")
for index, item in enumerate(narr):
    print(index, item)

print("*" * 40)
narr_multi = np.arange(0,6).reshape(2,3)
print(narr_multi)

print("*" * 40 , "iterating through multidimensional dimensional array")
for item in narr:
    print(item)
