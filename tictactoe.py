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
            print("Wrong format")
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

def get_move(board, size, state):
    input("\n{}'s next move: ".format('X' if state == X_TURN else 'O'))

def step_board(board, size, state):
    pass

def main():

    # Print title
    print("Advanced TicTacToe Game")

    # Set the board size from user input
    size = get_board_size()

    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create nested list for storing board state
    board = [['.'] * size for _ in range(size)]
    state = X_TURN

    while(state == X_TURN or state == O_TURN):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board, size)
        get_move(board, size, state)
        step_board(board, size, state)

    if(X_WON):
        print("X won the game, congratulations")
    else:
        print("O won the game, congratulations")






main()