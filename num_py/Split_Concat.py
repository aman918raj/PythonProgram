_author_ = "aman"
import numpy as np

a = np.arange(24).reshape(4,6)
print(a)

print("#####Split#####")

print("splitting a into 2 matrices \n{}".format(np.split(a , 2)))
print("splitting and getting 0th element \n{}".format(np.split(a,2)[0]))
print("splitting and getting 1st element \n{}".format(np.split(a,2)[1]))