import random

print("Dice Rolling Simulator")

while True:
    roll=input("Press Enter to Roll the Dice or Type 'Quit':")
    if(roll=='Quit'):
        print("---GOODBYEE---")
        break
    else:
        dice=random.randint(1,6)
        print("You rolled:",dice)