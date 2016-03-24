from Board import Board 
import sys

EMPTY = '.'
Player1 = '1'
Player2 = '2'


def main(arg):
    if(len(arg)<3):
        print("Insufficient argument specified")
        sys.exit()
        
    g = Board(int(arg[0]), int(arg[1]), int(arg[2]))
    option = raw_input("Do you want to load previous game (y/n): ")
    if (option=="y" or option=="Y"):
        g.LoadGame()    
        
    turn = Player1
    while True:
        g.printBoard()
        row = input('{}\'s turn: '.format('Player1' if turn == Player1 else 'Player2'))
        g.insert(int(row), turn)
        turn = Player2 if turn == Player1 else Player1
        
if __name__ == '__main__':
    main(sys.argv[1:])
        
        
