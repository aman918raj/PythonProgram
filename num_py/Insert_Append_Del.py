_author_ = "aman"
import numpy as np

print("######### APPEND ###########")
print("###### 1D #########")
a = np.array([4,9,5,12,6,7,9,77,4])
b = a.reshape(3,3)
print(a)
print(np.append(a, [20]))
print(np.append(a, [34,45]))
print(a) #--> create new np array everytime and decompose the old one

print("#### 2D ########")
print("normal append {}".format(np.append(b , [21,22,23]))) #appends and create 1d np array
print("add a row \n{}".format(np.append(b, [[21,22,23]], axis=0)))
#axis 0 is x and axis 1 is y
print("add a column \n{}".format(np.append(b, [[21],[22],[23]], axis=1)))

print("######INSERT#######")
print("Inserting in 1d array \n{}".format(np.insert(a , 3, 500)))
print("Inserting in 2d array \n{}".format(np.insert(b , 3, 500)))
print("Inserting in 2d array axis = 0\n{}".format(np.insert(b , 1, 500, axis=0)))
print("Inserting in 2d array axis = 1\n{}".format(np.insert(b , 2, 500, axis=1)))

print("#######Delete#################")
print("Deleting in 1d array \n{}".format(np.delete(a , 3)))
print("Deleting in 2d array axis= 0 \n{}".format(np.delete(b , 2, axis=0)))
print("Deleting in 2d array axis= 1 \n{}".format(np.delete(b , 2, axis=1)))
