import random 
playing = True
number = str(random.randint(0,9))
print("i will creat a game to guess the number between 0,9 one digit at a time!!")

while playing:
    guess = input("Give me your best guess")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("your guess is wrong try again!")