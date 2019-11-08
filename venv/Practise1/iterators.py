_author_='aman'

string = "1234567890"
for i in string:
    print(i)

iterator = iter(string)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#for loop is internally running iterator object
#below two for loops has same functionality and implementaions

for char in string:
    print(char)

for char in iter(string):
    print(char)
