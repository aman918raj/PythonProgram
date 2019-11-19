_author_ = "aman"

print(2 or 5)
print(not("0"))
def print_something():
    print("Hello World")

print_something()
print(print_something()) # --> prints two line one Hello World and other None. None because function print_something returns nothing

def add(a,b):
    print("sum of a and b is {0}".format(a + b))

add(3, 4)

def multiply(x, y):
    z = x * y
    return z

m = multiply(3, 4)
print("multiplication of 3 and 4 is {0}".format(m))

def reverse_string(word):
    reversed_word = ''
    i = 0
    for w in word:
        i = i + 1
        reversed_word = reversed_word + word[len(word)-i]
    return reversed_word

word = "word"
reversed_word = reverse_string(word)
print(reversed_word)
