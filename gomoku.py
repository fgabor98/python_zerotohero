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

    while True:
        size_in = input("Select board size (between {} and {}): ".format(MIN_SIZE, MAX_SIZE))
        if size_in.isdigit():
            if int(size_in) in range(MIN_SIZE,MAX_SIZE+1):
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

    while True:
        move = input("{}'s next move: ".format('X' if state == X_TURN else 'O'))
        col = move[0].upper()
        row = move[1:]
        if(col.isalpha() and row.isdigit()):
            col_num = string.ascii_uppercase.index(col)
            row_num = int(row) - 1
            if(col_num in range(0,size) and row_num in range(0,size)):
                if board[row_num][col_num] == '.':
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


LENGTH=5
def check_state(board, size, state):

    for (pos_y,row) in enumerate(board):
        for (pos_x,_) in enumerate(row):
            #Check horizontal
            check_hor = []
            check_ver = []
            check_diag_right = []
            check_diag_left = []
            for i in range(0,LENGTH):
                if(pos_x < size - LENGTH + 1):
                    check_hor.append(board[pos_y][pos_x+i])
                if(pos_y < size - LENGTH + 1):
                    check_ver.append(board[pos_y+i][pos_x])
                if(pos_x < size - LENGTH + 1 and pos_y < size - LENGTH + 1):
                    check_diag_right.append(board[pos_y+i][pos_x+i])
                if(pos_x >= LENGTH - 1 and pos_y < size - LENGTH + 1):
                    check_diag_left.append(board[pos_y+i][pos_x-i])

            if (len(check_hor) > 0 and all(element == 'X' for element in check_hor)):
                return X_WON
            if (len(check_ver) > 0 and all(element == 'X' for element in check_ver)):
                return X_WON
            if (len(check_diag_right) > 0 and all(element == 'X' for element in check_diag_right)):
                return X_WON
            if (len(check_diag_left) > 0 and all(element == 'X' for element in check_diag_left)):
                return X_WON
            if (len(check_hor) > 0 and all(element == 'O' for element in check_hor)):
                return O_WON
            if (len(check_ver) > 0 and all(element == 'O' for element in check_ver)):
                return O_WON
            if (len(check_diag_right) > 0 and all(element == 'O' for element in check_diag_right)):
                return O_WON
            if (len(check_diag_left) > 0 and all(element == 'O' for element in check_diag_left)):
                return O_WON
    return state


def main():

    # Print title
    print("Gomoku Game (5 in a row)")
    print("First player to get 5 symbols connected in a row, column or diagonal, wins")

    # Set the board size from user input
    size = get_board_size()

    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create nested list for storing board state
    board = [['.'] * size for _ in range(size)]
    print_board(board, size)
    state = X_TURN

    while state in (X_TURN, O_TURN):
        step_board(board, size, state)
        state = (X_TURN if state == O_TURN else O_TURN)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board, size)
        state = check_state(board, size, state)

    if state == X_WON:
        print("X won the game, congratulations")
    else:
        print("O won the game, congratulations")


if __name__ == "__main__":
    main()
