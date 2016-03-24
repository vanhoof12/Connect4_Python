from itertools import groupby, chain
import sys

EMPTY = '.'
Player1 = '1'
Player2 = '2'

def ForwardDiagonal (board, cols, rows):
    for di in ([(j, i - j) for j in range(cols)] for i in range(cols + rows -1)):
        yield [board[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

def BackwardDiagonal (board, cols, rows):
    for di in ([(j, i - cols + j + 1) for j in range(cols)] for i in range(cols + rows - 1)):
        yield [board[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]




class Board:
    def __init__ (self, cols = 7, rows = 6, length_to_win = 4):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.win = length_to_win
        self.board = [[EMPTY] * rows for _ in range(cols)]

    def insert (self, column, turn):
        """Insert the turn in the given column."""
        c = self.board[column]
        if c[0] != EMPTY:
            raise Exception('Column is full')

        i = -1
        while c[i] != EMPTY:
            i -= 1
        c[i] = turn

        self.checkForWin()

    def checkForWin (self):
        """Check the current board for a winner."""
        w = self.getWinner()
        if w:
            self.printBoard()
            print(w + ' won!')
            option = raw_input("Do you want to save this game? (y/n): ")
            if(option=="y" or option=="Y"):
                            filename = raw_input("Enter file name: ")
                            f = open(filename, 'w')
                            for i in range(0, self.rows):
                                for j in range(0, self.cols):
                                    f.write(self.board[i][j] + " ")
                                f.write("\n")
                            f.close()
            sys.exit()

    def getWinner (self):
        """Get the winner on the current board."""
        lines = (
            self.board, 
            zip(*self.board), 
            ForwardDiagonal(self.board, self.cols, self.rows),
            BackwardDiagonal(self.board, self.cols, self.rows) 
        )

        for line in chain(*lines):
            for turn, group in groupby(line):
                if turn != EMPTY and len(list(group)) >= self.win:
                    return turn

    def LoadGame(self):
        filename = raw_input("Enter file name: ")
        i = 0
        j = 0
        
        with open(filename, 'r') as f:
            for line in f:
                s = line.split(' ')
                for r in range (0, len(s)-1):
                    self.board[i][j] = s[r]
                    j = j + 1
                    
                i = i + 1
                j = 0
        f.close()
        
    def printBoard (self):
        print('  '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print('  '.join(str(self.board[x][y]) for x in range(self.cols)))
        print()

