_author_ = "aman"
import pandas as pd

days = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct", "Nov","Dec"]

a = pd.Series(days,months)

print("####Sorting by values ascending###")
print("sort values \n{}".format(a.sort_values()))

print("####Sorting by values descending###")
print("sort values \n{}".format(a.sort_values(ascending=False)))

print("####Sorting by index ascending###")
print("sort index \n{}".format(a.sort_index()))

print("####Sorting by index descending###")
print("sort index \n{}".format(a.sort_index(ascending=False)))

print("Original Value \n{}".format(a))
# The above sorting will not change our original value
#If we assign it to any other variable then the new variable will have the sorted value or we can use inplace
####Inplace

a.sort_values(inplace=True)
print("Value of a changed because we used inplace \n{}".format(a))
print(a.index)
a.sort_index(inplace=True)
print(a)