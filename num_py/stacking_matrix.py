_author_ = "aman"
import numpy as np

a = np.random.random(size=(3,3))
b = np.random.random(size=(3,3))
print(a)
print(b)
print("#####" * 50)

#horizontally stacking the matrices....Note--> all the matrices
# should have same number of rows for horizontal stacking
print(np.hstack((a,b)))
print("####" * 50)

#vertically stacking the matrices....Note--> all the matrices
# should have same number of columns for horizontal stacking
print(np.vstack((a,b)))
print("####" * 50)
##################################
a = 10 * a
print(a)
print("#######"*50)
#########floor and ceil###########
print(np.floor(a))
print(np.ceil(a))
print("#######"*50)
##############################
c = np.floor(a)
######sum of all the elements of a matrix
print("sum of all the elements of a matrix")
print(np.sum(c))
print("#######"*50)
######sum of all the elements of a particular row
print("sum of column wise")
print(np.sum(c, axis=0))
print("#######"*50)
########
print("sum of row wise")
print(np.sum(c, axis=1))
print("#######"*50)
########mean######
print("mean {0}".format(np.mean(c)))
print("mean column wise {0}".format(np.mean(c, axis=0)))
print("mean row wise {0}".format(np.mean(c, axis=1)))
print("#######"*50)
##########cumulative sum#######
print("cumulative sum {0}".format(np.cumsum(c)))
print("#######"*50)
######unique value#######
print("unique value {0}".format(np.unique(c)))