_author_="aman"
t = "a","b","c"
print(t)
print("a","b","c")
print(("a","b","c"))

welcome = ("welcome","to","python")
print(welcome)
print(welcome[1])
#welcome[0] = "wel" --> is not supportable because tupples are immutable but we can do it like below
welcome = ("wel",welcome[1], welcome[2]) #--> right hand side is evaluted before right hand side
print(welcome)

#unpacking tupple -->
greet, to, py = welcome
print(greet)
print(to)
print(py)

#tupple is immutable but if it contains list then list value can change -->
album = ("band1", 2014, [(1,"song1"), (2,"song2")])
print(album)
bandname , year, tracks = album
tracks.append((3,"song3"))
print(album)