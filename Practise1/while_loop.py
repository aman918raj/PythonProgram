_author_='aman'

i=0
while i<10:
    print(i)
    i+=1

directions = ['north', 'south', 'east', 'west']
choose_direction =''
while choose_direction not in directions:
    choose_direction = input("choose the correct direction: ")
    print(choose_direction)

