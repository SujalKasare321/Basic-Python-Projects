import random

target=random.randint(1,100)

while True:
    userChoice=input("Guesss the Target or Quit:")
    if(userChoice=="Quit"):
        break

    userChoice=int(userChoice)
    
    if(userChoice==target):
        print("SUCCESS : Corret Guess!!!")
        break
    elif(userChoice<target):
        print("your number was too small.Take a bigger guess...")
    else:
        print("your number was too big.Take a smaller guess...")

print("-----GAME OVER-----")