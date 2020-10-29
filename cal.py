##exercise modules
from random import randint
answer = randint(0,99)#rand int from 0-99
guess = -1
print(guess)
print(answer)

while guess != answer:
    guess=int(input("guess: "))
    if guess < answer:
        print("higher")
    elif guess > answer:
        print("lower")
print("correct")
