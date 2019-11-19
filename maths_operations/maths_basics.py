_author_ = "aman"
import math

#####finding cosine#######
cosine = math.cos(23)
print(cosine)

#####finding power in 3 different ways#######
power = math.pow(2,6)
print(power)

power2 = 2

for i in range(1,6):
    power2 = power2 * 2

print(power2)
print(2 ** 6)

########Extracting 'am' from a string##########
var = "I am learning python"
print(var[2:4])
print(var.split(" ")[1])

######Extract 'some' from a list#####
list = [1,2,3,[4,5,['some','object'],33.9], 'x']
print(list[3][2][0])

#####Remove 33.9 from the above list########
list[3].remove(33.9)
print(list)

#######Remove last element from the above list######
list.pop()
print(list)
