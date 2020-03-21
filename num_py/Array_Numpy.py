_author_ = "aman"
import numpy as np

py_list = [1,4,2,45]
print("Python List {0}".format(py_list))
numpyArray = np.array(py_list)
print("num py array {0}".format(numpyArray))
a  = np.array([[1,9,8,3], py_list])
print("num py array 2 {0}".format(a))
print(a)

b = np.array([[1,2,3,4], [5,6,7,8]])
print(b)

c = np.array([[1,2,3,4], [5,6,7]])
print(c)
print("#########" * 40)
# eye() only generates square matrix always with diagonal 1 value and having n*n matrix
np_eye = np.eye(4)
print(np_eye)
print(10 * np_eye)
# zero() can generate rectangular matrix
print("#########" * 40)
np_zero = np.zeros(shape=(4,6))
print(np_zero)
#ones() similar to zero but instead of 0 it has 1
print("#########" * 40)
np_one = np.ones(shape=(4,6))
print(np_one)
#arange() acts as range
print("#########" * 40)
print(np.arange(5))
print(np.arange(5,10))
print(np.arange(5,10,2))
print(np.arange(100,10,-5))
#linspace() divides array in equal space (creates equal partitions)
print(np.linspace(0,20,5))
print("####" * 50)
print(np.random.rand(2,3)) #generantes random num or int into 2 rows and 3 columns
print(np.random.randn(2,3)) #generantes random num into 2 rows and 3 columns
print(np.random.randint(10,20)) #generates one random int value between 10 to 20
print(np.random.randint(10,50,5)) #generates five random int value between 10 to 20
##################################
mat=np.random.rand(2,3)
print("size of matrix mat {0}".format(mat.size))
print("shape of matrix mat {0}".format(mat.shape))
print("data type of matrix {0}".format(mat.dtype))
