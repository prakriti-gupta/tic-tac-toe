#!/usr/bin/python3
import random
# from tkinter import *
# from graphics import *

# import tkinter.messagebox
# tk=Tk()
# tk.title("Tic Tak Toe")

# click = True

def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[1] + "|" + board[2] + "|" + board[3])


def player_input():
    marker = ''
    print('Enjoy playing Tic Tac Toe')
    while not (marker == 'X' or marker == '0'):
        marker = input('Palyer 1 chooses X or 0: ')

    if marker == 'X':
        return 'X', '0'
    else:
        return '0', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not (space_check(board, position)):
        position = int(input('Chose position between 1 to 9'))

    return position


def reply():
    choice = input('Do you want to play again :(Y/N)')

    if choice == 'Y':
        return True
    else:
        print('Thanks for playing (: ')



print('Welcome to the world of Tic Tak Toe (: ')


while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play = input('Ready to play (y/n)')
    if play == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Player1 has won')
                game_on = False
            else:
                if full_board_check(board):
                    print('Game is tie between both the players')
                    game_on = False
                else:
                    turn = 'Player2'

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Player2 has won')
                game_on = False
            else:
                if full_board_check(board):
                    print('Game is tie between both the players :---:')
                    game_on = False
                else:
                    turn = 'Player1'

    if not reply():
        break
