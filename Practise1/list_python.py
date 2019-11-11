from typing import List, Union

_author_='aman'

char_list = ['a','x','f','o']
char_list.append('v')
print(char_list)

even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = even + odd
print(numbers)
numbers.sort()
print(numbers)
numbers_sort = sorted(numbers)
#print(numbers.sort()) <-- returns "none" because sort function or append function or any function
# on list applies on variable or object but it doesnot create new object.
#to sort we have built in function in Python "sorted"
#print(sorted(numbers))
if numbers == numbers_sort:
    print("The lists are equal")
else:
    print("The lists are not equal")

list_1 = []
list_2 = list()
print("List 1 is {}".format(list_1))
print("List 2 is {}".format(list_2))

if list_1 == list_2:
    print("Lists are equal")
else:
    print("Lists are not equal")

print(list("This is a list"))

even_2 = [2,4,6,8]
another_even = even_2
another_even_2 = list(even_2)

another_even.sort(reverse=True)
print(another_even is even_2)
print(another_even_2 is even_2)

print(even_2)
print(another_even)
#In the above case both another_even and even_2 are referring and pointing to the same value and variable
#but the below function sorted is created a new variable or object
another_even_3 = sorted(even_2, reverse=True)
print(another_even_3 is even_2)

numbers_2 = [even,odd]
print(numbers_2) # <-- returns list of lists (A list containg two list list even and list odd)

welcome = ["welcome",2,"python"]
print(welcome)
welcome[0] = "wel" #list is  mutable
print(welcome)
