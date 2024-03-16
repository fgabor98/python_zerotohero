#!/usr/bin/env python3
import os
import string

MIN_SIZE = 10
MAX_SIZE = 20

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
    print('     ', end='')
    for num in range(size):
        print('{}'.format(num), end=' ')
    print()
    print('   ', end='')
    print('_' * (size * 2 + 1))
    for (num,row) in enumerate(board):
       print('{}  |'.format(string.ascii_uppercase[num]), end=' ')
       for cell in row:
           print(cell, end=' ')
       print()

def main():

    # Print title
    print("Advanced TicTacToe Game")

    # Set the board size from user input
    size = get_board_size()

    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create nested list for storing board state
    board = [['.'] * size] * size
    board[3][4] = 'X'
    print_board(board, size)






main()