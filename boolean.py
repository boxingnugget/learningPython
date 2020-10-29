name = 'michael'
tries = 0
while tries < 3:
    guess = input("guess my name: ")
    if guess == name:
        print("that's right!")
        break
    else:
        tries += 1
        if tries == 3:
            print("you lose")
