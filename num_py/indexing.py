_author_ = "aman"
import numpy as np

arr = np.arange(20,40)
print(arr)
print("printing the size of an array {}".format(arr.size))
print("printing the shape of an array {}".format(arr.shape))
print("printing first element {}".format(arr[0]))
print("printing fourth element {}".format(arr[4]))
print("printing last element {}".format(arr[-1]))
print("slicing an array 24 to 39 {}".format(arr[4 : -1]))
print("slicing an array 22 to 22 {}".format(arr[2 : 3]))
print("slicing an array 22 to 25 {}".format(arr[2 : 6]))
print("slicing an array 20 to 25 {}".format(arr[ : 6]))
print("slicing an array 20 to 39 {}".format(arr[ : 39]))
print("slicing an array 20 to 38 {}".format(arr[ : -1]))
print("#" * 50)
gt_than_35 = arr > 35
print("checking element greater than 35 {}".format(gt_than_35))
print("#" * 50)
mul_elements = arr * 2
print("multiplying each elemet by 2 {}".format(mul_elements))
