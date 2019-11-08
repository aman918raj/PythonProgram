_author_='aman'
print(range(100))
my_list = list(range(10))
print(my_list)

even = range(0,10,2)
odd = range(1,10,2)
print(even)
print(odd)

my_string = "abvjl34jflkems"
print(my_string.index('v'))
print(my_string[2])

numbers = range(13)
new_range = numbers[1::2]
print(new_range)
for i in new_range:
    print(i, end=',')

my_range = range(1,20)
for i in my_range:
    print(i)

my_range1 = my_range[1::2]
for i in my_range1:
    print(i)

my_range2 = my_range[::-1]
for i in my_range2:
    print(i)

my_range3 = my_range[19::-2]
for i in my_range3:
    print(i)
