_author_ = "aman"
# sets can be defined like dictionary using curly braces or using set keyword

animal = {"cow", "lion", "dog", "elephant"}
print(animal)
colour = set(["blue", "orange", "white", "green"])
print(colour)

print("-"*40)

animal.add("horse")
colour.add("red")
print(animal)
print(colour)

numbers = set([0,1,2,3,4,5,6,7,8,9])
even = set([0,2,4,6,8])
odd = set([1,3,5,7,9])
print(numbers.intersection(even))
print(even.union(odd))
