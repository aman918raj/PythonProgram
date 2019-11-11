_author_ = "aman"

import pickle

album = ('abcd' , '2011', ((1,'song'),(2,'song2')))
even = list(range(0, 10,2))
odd = list(range(1, 10, 2))

with open("C:\\Users\\aman.raj\\Desktop\\python_output\\album.pickle","bw") as pickle_file:
    pickle.dump(album, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(273839, pickle_file)

with open("C:\\Users\\aman.raj\\Desktop\\python_output\\album.pickle","br") as album_pickled:
    album2 = pickle.load(album_pickled)
    even_list = pickle.load(album_pickled)
    odd_list = pickle.load(album_pickled)
    x = pickle.load(album_pickled)

print(album2)
album_name, year, tracks = album2
print(album_name)
print(year)
print(tracks)
for track in tracks:
    track_number, track_name = track
    print(track_number)
    print(track_name)

print("=" * 40)

for i in even_list:
    print(i)

print("=" * 40)

for i in odd_list:
    print(i)

print("=" * 40)

print(x)
