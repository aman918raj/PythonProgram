_author_ = "aman"
import pandas as pd

days = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct", "Nov","Dec"]

a = pd.Series(days,months)
#Python builtin functions
print(type(a))
print(dict(a))
print(max(a))
print(min(a))
print(sum(a))

#Extarct values

print("getting only 1st value : {}".format(a[0]))

print("getting value by using index : {}".format(a["Feb"]))

print("get values till May : \n{}".format(a[:5]))

print("get values from March to Oct : \n{}".format(a[2:10]))

print("get Jan, Mar, Dec values : \n{}".format(a[[0,2,11]]))

print("get Dec value : \n{}".format(a[-1]))

print("get values from Nov to Jul \n{}".format(a[-2:-6]))