_author_ = "aman"
fruits = {"orange": "a sweet, organge, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a citrus fruit",
          "grape": "a green, sweet fruit",
          "mango": "yellow, sweet"
          }
print(fruits)

veg = {"potato": "brown",
       "spinach": "green",
       "sprouts": "green",
       "cabbage": "green"}
print(veg)

veg_fruit = fruits.update(veg) # --> create none object because update method updates the same object on which its called
print(veg_fruit)
print(fruits)
print(veg)

veg_fruit2 = fruits.copy()
veg_fruit2.update(veg)
print(veg_fruit2)
