_author_ = "aman"

cities = ["Delhi", "Mumbai", "Bengaluru", "Kolkata", "Chennai"]
with open("C:\\Users\\aman.raj\\Desktop\\python_output\\file1.txt","w") as city_file:
    for city in cities:
        print(city, file=city_file)

cities1 = []
with open("C:\\Users\\aman.raj\\Desktop\\python_output\\file1.txt","r") as city_file1:
    for city in city_file1:
        cities1.append(city)

print(cities1)
for city in cities1:
    print(city.strip("\n"))

album = ("band1", 2014, (1,"song1"), (2,"song2"))
with open("C:\\Users\\aman.raj\\Desktop\\python_output\\file2.txt","w") as city_file:
        print(album, file=city_file)

with open("C:\\Users\\aman.raj\\Desktop\\python_output\\file2.txt", "r") as city_file:
    contents = city_file.readline()

albums = eval(contents)
print("*"*50 )
print(albums)
band, year, song1, song2 = albums
print(band)
print(year)
print(song1)
print(song2)