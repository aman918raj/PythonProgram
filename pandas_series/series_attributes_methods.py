_author_ = "aman"
import pandas as pd

a = pd.read_csv("stock.csv", squeeze=True, usecols=["High"])
print(a)

print(a.index)
print(a.values)

###anything which does not have braces are attributes
# like index, values are attributes but read_csv is method

print(a.dtype)
print(a.ndim)
print(a.size)
print(a.shape)

print(a.is_monotonic_increasing)

s = a.add_prefix('panda')
print("print s with prefix index \n{}".format(s))

s = a.add_suffix("panda")
print("print s with suffix index \n{}".format(s))

print(s.sum())

print(a)

####a does not have suffix but s has because we have assigned it to s.
# In python, original value of any object does not change because of "inplace"
print("index of maximum value {}".format(s.idxmax()))#index of max value
print(max(s)) #max value of s
print("index of minimum value {}".format(s.idxmin()))#index of min value
print("head \n{}".format(s.head())) #shows the first 5 values
print("tail \n{}".format(s.tail())) #shows the last 5 values

print("head 3 values\n{}".format(s.head(3))) #shows the first n values
print("tail 2 values\n{}".format(s.tail(2))) #shows the last n values

print("mean \n{}".format(s.mean()))
print("product \n{}".format(s.product()))
print("standard deviation \n{}".format(s.std()))
