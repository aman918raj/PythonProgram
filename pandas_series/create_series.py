_author_ = "aman"
import pandas as pd

lst = [4,6,2, "abc"]
print(pd.Series(lst))

print(pd.Series(5))

print(pd.Series(5, index=[0]))

print(pd.Series(4, index=[0, 1, 2 , 40, 21]))

a = pd.Series([num*10 for num in range(10)])
print(a)

dict = {"a": "4829422", "b":"43242", "c":"83939"}
print(pd.Series(dict))
########Series cannot accept set object