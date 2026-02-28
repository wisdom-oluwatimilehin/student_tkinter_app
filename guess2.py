import random


points = 100
won = False
next = False

while True:
    if points > 0:
        print("Welcome, guess the correct number to win a point")
        print("you can guess from range 1-10")
        guess = int(input("Guess a number: "))
        real1 = random.randint(1,10)
        if real1 == guess:
            print("you guessed correctly")
            print("You can now proceed to the next level")
            points += 30
            print("You now have ",points,"points")
            won = True
            break
        else:
            points -= 20
            print("Try again, the actual answer is", real1)
            print("You now have ",points,"points")
            
    elif points <= 0:
        print("You don't have enough points to continue the game")
        won == False
        break

while True:
    if won == True and points > 0:
        guess2 = int(input("guess a new number: "))
        print("you can guess from range 11-20")
        real2 = random.randint(11,20)
        if real2 == guess2:
            print("You guess correctly again")
            print("You can now proceed to the final level")
            points += 30
            print("You now have ",points,"points")
            won = False
            next = True
            break

        else:
            points -= 50
            print("Try again the correct answer is",real2)
            print("You now have", points,"points")

            
    elif points <= 0:
        print("You don't have enough points to continue the game")
        won == False
        break
    
while True:
    if next == True and points > 0:
        guess3 = int(input("guess the final number: "))
        print("you can guess from range 21-30")
        real3 = random.randint(21,30)
        if real3 == guess3:
            print("You guess correctly again")
            print("You can now proceed to the final level")
            points += 40
            print("You now have ",points,"points")
            won = False
            next = True
            break
        else:
            points += 60
            print("Try again the correct answer is",real3)
            print("You now have ",points,"points")
            
    elif points <= 0:
        print("You don't have enough points to continue the game")
        next == False
        break
    

