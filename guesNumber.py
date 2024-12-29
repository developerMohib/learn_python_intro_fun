import random

randomNumber = random.randrange(1, 10)

guesNumber = int(input("Please give any number from 1 to 10 :"))

if randomNumber > guesNumber:
    print(f"The random number is {randomNumber} 🤗")
    print("Your given number is not match, and it big than random number 🤔")
elif guesNumber > randomNumber:
    print(f"The random number is {randomNumber}")
    print("Your given number is not match, and it small than given number 🤔")

else:
    print(f"Congrantulations your number and random number is match 😱👌")
