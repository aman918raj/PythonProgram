_author_ = "aman"
import numpy as np

mat1 = np.array([[1,4],[2,3]])
print(mat1)

###linalg is used for linear algebra related functionality######
print("determinant {0}".format(np.linalg.det(mat1)))
print("inverse \n {0}".format(np.linalg.inv(mat1)))
print("transpose \n {0}".format(np.transpose(mat1)))
print("trace {0}".format(np.trace(mat1)))#-- trace is sum of first diagonal elements
print("#########")

mat2 = np.arange(11,20).reshape(3,3)
print(mat2)
print("transpose {0}".format(np.transpose(mat2)))
print("determinant {0}".format(np.linalg.det(mat2)))
print("inverse {0}".format(np.linalg.inv(mat2)))
print("matrix multiplication {}".format(mat1.dot(mat1)))

print("#######linear equation#########")
#Consider the two linear equation below:
# 2x + y = 1
#  x + y = 2
# we need to create two matrices to find x and y. one for LHS and another for RHS
m0 = np.array([[2,1],[1,1]]) #for LHS
m1 = np.array([1,2]) #for RHS
m2 = np.linalg.solve(m0,m1)
print("solution is {}".format(m2))

print("######Eigen value and eigen vector############")
eigVal, eigVector = np.linalg.eig(m0)
print("Eigen Value {}".format(eigVal))
print("Eigen Vector {}".format(eigVector))