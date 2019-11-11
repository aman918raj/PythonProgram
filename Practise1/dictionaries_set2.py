_author_ = "aman"
fruits = {"orange": "a sweet, organge, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a citrus fruit",
          "grape": "a green, sweet fruit",
          "mango": "yellow, sweet"
          }

# for i in range(10):
#     for fruit in fruits:
#         print("{0} is {1}".format(fruit,fruits))
#     print("-"*40)

lst_keys = sorted(list(fruits.keys()))
print(lst_keys)
for i in lst_keys:
    print(i, fruits[i])

for i in fruits.values():
    print(i)

print(fruits.keys())
print(fruits.values())

fruit_keys = fruits.keys()
fruits["banana"] = "green when young and yellow when old"
print(fruit_keys)
f_tuple = tuple(fruits.items())
print(f_tuple)