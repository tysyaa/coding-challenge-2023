#!/usr/bin/env pyhton

#hanna,amelia
import random

def main():
    """Start a music guessing game."""
    print("Guess the justin bieber song!")
# mengisytiharkan 
    song = [
      "baby",
      "sorry",
      "yummy",
      "love me",
      "ghost",
      "never say never",
      "boyfriend"
      ]

    x = random.choice(song)
    
    guess = None
# memulakan gelung game
    while x != guess:

        guess = str(input("What song am i thinking of? "))

        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please put another justin bieber song!".format(guess))

main()