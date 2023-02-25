import sys
import time
import random

def printWord(word):
    newWord = ""
    for i in range(0, len(word)):
        newWord += word[i] + " "
    print(newWord)

# Hangperson

while True:

    words = ["book","cat","dog","computer"]

    word = random.choice(words)
    visibleWord = []

    won = ""

    for i in range(0, len(word)):
        visibleWord.append(i)
        visibleWord[i] = "*"

    print("Welcome!")
    print("")

    print("Here is the word.")
    print("")
    time.sleep(2)
    printWord(visibleWord)
    print("")

    #print(visibleWord)
    #print(word)

    time.sleep(2)

    attempts = 0
    maxAttempts = 10

    while True:

        if maxAttempts == attempts:
            won = "max attempts"
            break

        completed = True
        for i in range(0, len(visibleWord)):
            if visibleWord[i] == "*":
                completed = False

        if completed == True:
            won = "completed"
            break
                

        print("You have " + str(maxAttempts - attempts) + " attempts remaining.")
        
        guessWord = input("Please enter a letter to guess:")
        guessLetter = guessWord[0].lower()

        isLetter = False

        for i in range(0, len(word)):
            if word[i] == guessLetter:
                isLetter = True
                visibleWord[i] = word[i]

        if isLetter:
            print("That letter is correct! You have gained an extra attempt.")
        else:
            print("That letter is not correct!")
            attempts += 1

        time.sleep(2)

        print("")
        printWord(visibleWord)
        print("")

        time.sleep(2)

    if won == "completed":
        print("")
        print("Congrats! You have won!!")
    elif won == "max attempts":
        print("")
        print("You lost! You ran out of attempts.")

    retry = input("Would you like to play again? (Y/N)")

    if retry == "N" or retry == "n":
        sys.exit()
    else:
        print("")
        
    
        
            

        

        

        

    
