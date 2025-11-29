import random


print("-----ROCK PAPER SCISSORS GAME-----")

while True:
    move=input("Enter your move(Rock,Paper,Scissor) or Type 'Quit':")

    l=["Rock","Paper","Scissor"]

    if(move=='Quit'):
        print("Thanks for playing!!!")
        break
    if(move not in l):
        print("Invalid Move,TRY AGAIN!")
        continue

    ans=random.choice(l)
    print("My chance:",ans)
    
    if(move==ans):
        print("DRAW")
    elif(move=="Rock"and ans=="Scissor") or (move=="Scissor" and ans=="Paper") or (move=="Paper" and ans=="Rock"):
        print("YOU WIN")
    else:
        print("YOU LOSE")