_author_ = "aman"
import numpy as np

a = np.array([4,3,7,5])
b = a
print(a , b)
a[0] = 2

print(a , b) #when any value in a changes then corresponding value in b also changes because
             # b is view of a. It doesnt create new array b instead it just creates a view on top of a

print("### find memory address of a and b ######")
#id function is used to find memory address
print(id(a) , id(b)) #in this case both are using the same address because b is just aview on top of a
# we can also create view using view function
c = a.view()
print(a , b , c)
print(id(a) , id(b), id(c))

c[2]=100
print(a , b , c)

print("###########COPY############")
x = a.copy()
print(a , x)
print(id(a) , id(x))
x[2] = 300
print(a , x)