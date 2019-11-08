_author_='aman'
print("please guess the number")
guess = int(input())

if guess < 5:
    print(str(guess)+"less than 5")
    print("please guess higher value")
    guess = int(input())
    if guess == 5:
        print("you have guessed it correct")
    else:
        print("Sorry you have guessed it wrong")
elif guess > 5:
    print(str(guess) + "greater than 5")
    print("please guess lower value")
    guess = int(input())
    if guess == 5:
        print("you have guessed it correct")
    else:
        print("Sorry you have guessed it wrong")
else:
    print("Correct answer")

age=int(input("How old are you "))
if  15 < age < 66:
    print("age is between 15 to 66")
else:
    print("age is less than 15 or greater than 66")