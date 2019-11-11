_author_='aman'
age = 28
#print("My age is "+age+" years") --> will throw an error with number and string in same print
print("My age is "+str(age)+" years")

print("My age is {0} years".format(age))
print("There are {0} days in month {1}, {2}".format(31,"January", "March"))

print("My age is %d years" % age)
print("My age is %d %s" %(age, "years"))

for i in range(1,5):
    print("No. %d squared is %2d and cubed is %3d" %(i, i*i, i*i*i))