_author_ = "aman"
import pandas as pd

a = pd.read_csv("test.csv")
print(a)
print(type(a))

b = pd.read_csv("test.csv", header=None)
print(b)

###using squeeze to convert dataframe into Series#####
print("###using squeeze to convert into Series#####")
c = pd.read_csv("test.csv", header=None, squeeze=True)
print(c)
print(type(c))

###read a particular column into Series#####
#squeeze is used to convert into series
print("###read a particular column into Series#####")
d = pd.read_csv("stock.csv", squeeze=True, usecols=["Open"])
print(d)
print(type(d))