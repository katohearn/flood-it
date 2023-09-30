import sys
import string
import random

# class to create game board

class GameBoard:

    def __init__(self, size, numColor):
        self.size = size
        self.numColor = numColor
        self.colors = [random.choice(string.ascii_uppercase) for i in range (numColor)]
        self.board = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                self.board[i][j] = random.choice(self.colors)
        
# turn counter

# read the current state of the game board

# given input from user, change the state of the game board

def main():

    size = 5
    numColor = 5
    
    gb = GameBoard(size,numColor)

    print("Game board size:", gb.size)
    print("Number of colors to use:", gb.numColor)
    print("Color representations:", gb.colors)
    print("Game board:", gb.board)

if __name__ == "__main__":
    main()