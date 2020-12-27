_author_ = "aman"
class Cars():

    power_source = "petrol"

    def __init__(self, model, wheels, doors):
        self.model = model
        self.wheels = wheels
        self.doors = doors
        self.on = False

    def engine_on(self):
        self.on = True

maruti = Cars("Swift",4,4)
print(maruti.wheels)
print(maruti.doors)
maruti.doors=5
print(maruti.doors)

tata = Cars("Zest",4,4)
print(tata.wheels)

print("Cars {}={}, {}={}".format(maruti.model, maruti.wheels, tata.model, tata.wheels))
print("Cars {0.model}={0.wheels}, {1.model}={1.wheels}".format(maruti, tata))

print(maruti.on)
maruti.engine_on()
print(maruti.on)

Cars.engine_on(tata)
print(tata.on)

maruti.power = 200
print(maruti.power)

#print(tata.power) --> will throw an error
print("###" * 50)
print(Cars.power_source)
print(maruti.power_source)
print(tata.power_source)

print("*********using dict*******")
print(Cars.__dict__)
print(maruti.__dict__)
print(tata.__dict__)