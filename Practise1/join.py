_author_ = "aman"
my_list = ["a", "b", "c", "d"]
# string is immutable, every time we iterate and add an element to string it creates
# a new object iternally
new_str = ''
for i in my_list:
    new_str += i + ","
print(new_str)

new_str1 = ",".join(my_list)
print(new_str1)

letters = "abcdefghijklmnopqrstuvwxyz"
new_str2 = ",".join(letters)
print(letters)
