_author_ = "aman"
import pandas as pd

days = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct", "Nov","Dec"]

#index and series can contain different kind of object

a = pd.Series(days)
print(a)
b= pd.Series(days, months) #here months are the index
print(b)
c = pd.Series(data=days,index=months)
print(c.index)