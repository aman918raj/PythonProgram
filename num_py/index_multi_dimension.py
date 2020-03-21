_author_ = "aman"
import numpy as np

#creating 5 X 6 matrix 5 rows and 6 columns
matrix = np.random.rand(5,6)
print("matrix {}".format(matrix))
print("#" * 50)

print("print 2nd row and 3rd element {}".format(matrix[1,2]))
print("#" * 50)
#printing one row
print(matrix[1,])
print(matrix[1])

print("#" * 50)
#slicing a column (i am taking last column)
print("print last column {}".format(matrix[:,5]))
print("#" * 50)

#slicing row 1,2,3 and all columns from them
print("slicing 3 rows and all columns \n{}".format(matrix[1:4, :]))
print("#" * 50)

#slicing all rows and first 2 columns
print("print all rows and first two columns \n{}".format(matrix[ : , 0:2 ]))

#slicing 4 rows from between the matrix like 3rd and 4th rows and 3rd and 4th columns
print("print 3rd and 4th rows and 2nd and 3rd columns \n{}".format(matrix[2:4 , 1:3]))

#finding cosine of each element
print(np.cos(matrix))

#finding the sum of all the element
print(np.sum(matrix))

#converting to lower integer
print(np.floor(matrix))

#converting to upper integer
print(np.ceil(matrix))

npc = np.ceil(matrix)

#find sum of a axis(row)
print(np.sum(npc, axis=0))

#find sum of a axis(row)
print(np.sum(npc, axis=1))

#finding the mean
print(np.mean(matrix))
print(np.mean(npc))

#cummulative sum
print(np.cumsum(npc))

#cummulative product
print(np.cumprod(npc))

#unique
print(np.unique(npc))

#min & max
print(np.min(matrix))
print(np.min(matrix, axis=0))
print(np.min(matrix, axis=1))