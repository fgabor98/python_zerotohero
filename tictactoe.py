#!/usr/bin/env python3
import os
import string

MIN_SIZE = 10
MAX_SIZE = len(string.ascii_uppercase)
X_TURN = 0
O_TURN = 1
X_WON = 2
O_WON = 3

def get_board_size():

    while(1):
        size_in = input("Select board size (between {} and {}): ".format(MIN_SIZE, MAX_SIZE))
        if(size_in.isdigit()):
            if(int(size_in) in range(MIN_SIZE,MAX_SIZE+1)):
                return int(size_in)
            else:
                print("Value not in allowed range")
                continue
        else:
            print("Format error")
            continue


def print_board(board, size):

    print('      ', end='')
    for num in range(size):
        print('{}'.format(string.ascii_uppercase[num]), end=' ')

    print('\n    ' + '_' * (size * 2 + 1))

    for (num,row) in enumerate(board):
       print('{:>2}  |'.format(num+1), end=' ')
       for cell in row:
           print(cell, end=' ')
       print()
    
    print()

def step_board(board, size, state):

    while(1):
        move = input("{}'s next move: ".format('X' if state == X_TURN else 'O'))
        col = move[0].upper()
        row = move[1:]
        if(col.isalpha() and row.isdigit()):
            col_num = string.ascii_uppercase.index(col)
            row_num = int(row) - 1
            if(col_num in range(0,size) and row_num in range(0,size)):
                if(board[row_num][col_num] == '.'):
                    board[row_num][col_num] = 'X' if state == X_TURN else 'O'
                    return
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_board(board, size)
                    print("Illegal move, enter again", end=' ')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board(board, size)
                print("Value out of range, enter again", end=' ')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(board, size)
            print("Format error, enter again", end=' ')


def check_state(board, size, state):

    #Check horizontals
    for row in board:
        for pos,cell in enumerate board[:-2]:
            if()




    return state


def main():

    # Print title
    print("Advanced TicTacToe Game")

    # Set the board size from user input
    size = get_board_size()

    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create nested list for storing board state
    board = [['.'] * size for _ in range(size)]
    print_board(board, size)
    state = X_TURN

    while(state == X_TURN or state == O_TURN):
        step_board(board, size, state)
        state = (X_TURN if state == O_TURN else O_TURN)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board, size)
        state = check_state(board, size, state)

    if(X_WON):
        print("X won the game, congratulations")
    else:
        print("O won the game, congratulations")





if __name__ == "__main__":
    main()