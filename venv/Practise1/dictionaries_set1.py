_author_ = "aman"
# ########################Dictionary and Set###############################
# They both are are unordered collections
# They both do not contain duplicates
# We cannot access an element in Set using an index. Its because its meaningless since it is unordered.
# Dictionary is like map which contain key value pairs. Value can be duplicate but not the key.
# Elements in Dictionay are accessed using Keys
# Dictionary can have any object in Python as key and value. But it should be immutable for e.g. key can be list or tupple... or value can be a list or tupple...
# Set and Dictionary elements are hashed
fruit = {"orange": "a sweet, organge, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a citrus fruit",
         "grape": "a green, sweet fruit"}
print(fruit)
print(fruit.get("lemon"))
print(fruit["lemon"])
fruit["lemon"] = "citrus and yellow in colour"
print(fruit)
fruit["banana"] = "green when young and yellow when old"
print(fruit)
del fruit["orange"]
print(fruit)
fruit.clear()
print(fruit)
# print(fruit["banana"]) --> will throw an error
lst_bikes = [{"Yamaha": {"brand": "Yamaha", "model": "FZ25", "engine": 250}},
             {"Honda": {"brand": "Honda", "model": "CBR", "engine": 250}}]
bike = {"bikes": lst_bikes}
print(bike)
print(bike["bikes"])
for bik in bike:
    print(bike[bik])
    for b in bike[bik]:
        print(b)
while True:
    dict_key = input("Please enter the vehicle type : ")
    if dict_key == "bikes":
        print(bike["bikes"])
        brand = input("Please enter the brand : ")
        if brand == "Yamaha":
            print(bike["bikes"][0]["Yamaha"])
        elif brand == "Honda":
            print(bike["bikes"][1]["Honda"])
        else:
            log1 = bike.get(dict_key)[0].get(brand, "We don't have a {0}".format(brand))
            print(log1)
            break
    else:
        log2 = bike.get(dict_key, "We don't have a {0}".format(dict_key))
        print(log2)
        break
