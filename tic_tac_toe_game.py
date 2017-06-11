# Python tic tac toe game

# import print function from python 3
from __future__ import print_function
from IPython.display import clear_output

# set up the board with a 3x3 grid size
# print out the board
# board is set up as a list
# index 1-9 corresponds to a board square, starting from the bottom left
def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# function to take in player input, and assign their marker as X or O
# the while loop ensures that the player is asked until they input a correct answer
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# take in a marker and position number
def place_marker(board, marker, position):
    board[position] = marker

# check to see if someone has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

# import and use the random module to randomly decide which player goes first
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# return a boolean indicating whether the board space is available or not
def space_check(board, position):
    return board[position] == ' '

# check if the board is full and return a boolean value
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# ask for a player's next position and if the position
# is available then return it for later use
def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your next position: (1-9) ')
    return int(position)

# ask player if they want to play again and return a boolean value
def replay():
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# start the game
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break