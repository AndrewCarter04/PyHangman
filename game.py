import time
import random
import sys

def cpuPlay(grid1):
    amount = 0
    while True:
        num = random.choice(grid1)
        amount += 1
        if not(num == "x" or num == "o"):
            break
        if amount == 1000:
            num = 101
            break
    return int(num) -1

def printGrid(grid):
    print("The current grid:")
    print("")
    print(grid[0] + " | " + grid[1] + " | " + grid[2])
    print(grid[3] + " | " + grid[4] + " | " + grid[5])
    print(grid[6] + " | " + grid[7] + " | " + grid[8])
    print("")
    

while True:
    print("Welcome!")
    print("")

    time.sleep(2)

    print("You will be playing against the computer, and you will be crosses.")
    print("")

    grid = ["1","2","3","4","5","6","7","8","9"]
    #availableGrid = ["1","2","3","4","5","6","7","8","9"]

    time.sleep(2)

    printGrid(grid)

    won = "no"

    while True:
        inputNum = ""
        while True:
            inputNum = input("Enter a number from the grid to replace it.")
            if inputNum.isnumeric():
                if int(inputNum) < 10 and int(inputNum) > 0:
                    if not(grid[int(inputNum) - 1] == "x" or grid[int(inputNum) - 1] == "o"):
                        break

        inputNum = int(inputNum)
                
             

        if grid[inputNum -1] == "x" or grid[inputNum - 1] == "o":
            print("That spot has already been used!")
            time.sleep(1)
            inputNum = int(input("Enter another number from the grid to replace it."))

        grid[inputNum - 1] = "x"
        #del availableGrid[inputNum - 1]
        time.sleep(1)
        printGrid(grid)

        if (grid[0] == grid[1] == grid[2] == "x") or (grid[3] == grid[4] == grid[5] == "x") or (grid[6] == grid[7] == grid[8] == "x") or (grid[0] == grid[3] == grid[6]  == "x") or (grid[1] == grid[4] == grid[7]  == "x") or (grid[2] == grid[5] == grid[8]  == "x") or (grid[0] == grid[4] == grid[8]  == "x") or (grid[2] == grid[4] == grid[6]  == "x"):
            print("YOU WON!!!")
            won = "yes"
            break

        if cpuPlay(grid) == 100:
            won = "no winner"
            break

        print("It is the computers turn.")
        time.sleep(2)
    
        grid[cpuPlay(grid)] = "o"
        printGrid(grid)

        if (grid[0] == grid[1] == grid[2] == "o") or (grid[3] == grid[4] == grid[5] == "o") or (grid[6] == grid[7] == grid[8] == "o") or (grid[0] == grid[3] == grid[6]  == "o") or (grid[1] == grid[4] == grid[7]  == "o") or (grid[2] == grid[5] == grid[8]  == "o") or (grid[0] == grid[4] == grid[8]  == "o") or (grid[2] == grid[4] == grid[6]  == "o"):
            print("YOU LOST!!!")
            won = "no"
            break

    if won == "yes":
        print("")
        print("You have beaten the computer! Congrats!")
    elif won == "no":
        print("")
        print("The computer has beaten you! Better luck next time.")
    elif won == "no winner":
        print("")
        print("There was no winner, better luck next time!")

    while True:
        print("")
        playAgain = input("Do you want to play again? (Y/N)")
        if playAgain == "y" or playAgain == "Y":
            print("")
            break
        elif playAgain == "n" or playAgain == "N":
            sys.exit()
            

    





