_author_ = "aman"

#formula for c to f conversion is :
# F = 32 + 1.8 * c

def c_to_F(c):
    F = 32 + 1.8 * c
    return F

farenheit = c_to_F(100)
print(farenheit)