import random

words = ["python", "hangman", "developer", "programming", "computer", "science"]

def hangman():
    w=random.choice(words)
    guessed=["_"]*len(w)
    attempts=6
    used_letters=[]
    
    print("---HANGMAN GAME---")
    print("Word:"," ".join(guessed))

    while attempts>0:
        guess=input("Guess a word:").lower()

        if not guess.isalpha() or len(guess)!=1:
            print("Please enter a single letter")
            continue

        if guess in used_letters:
            print("Already guessed...Try another word")
            continue
        used_letters.append(guess)

        if guess in w:
            print("Good guess :",guess," is correct")
            for i in range(len(w)):
                if w[i]==guess:
                    guessed[i]=guess

        else:
            attempts-=1
            print("Wrong guess :",guess," is not correct")
            print("Attempts remaining:",attempts)
        print("Word:"," ".join(guessed))
        print("Used words:",",".join(used_letters))

        if "_" not in guessed:
            print("CONGRATS!!! You guessed the word:",w)
            break

    else:
        print("You LOST :/  Better luck next time")
        print("The word was:",w)

hangman()
