# TODO: Write your name here.

import random

PLAYER = 'player'
COMPUTER = 'computer'


# Here are the empty functions that it's your job to implement!
# Check the assignment carefully to see what each function is supposed to do.
# Don't rename these functions! You can absolutely write extra functions aside from these
# ones if you want, but don't change the names of the five functions please.

def make_board():
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass


def print_board(board):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass


def get_player_move(board):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass


def get_computer_move(board, computer_team):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass


def check_for_winner(board):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass


# Now that we've defined our functions, let's play a game of tic-tac-toe!


# (Note: This `if` statement is important, please don't remove it.)
if __name__ == '__main__':
    print('Welcome to Tic-Tac-Toe!')

    # Ask the player what team they want to be.
    player_team = input('Do you want to be X or O?\n').upper()

    if player_team == 'X':
        computer_team = 'O'
    else:
        computer_team = 'X'

    # Decide who goes first.
    whose_turn = random.choice([PLAYER, COMPUTER])
    print('The {} will go first.'.format(whose_turn))

    # Get a fresh board.
    board = make_board()

    while True:
        # Figure out whose turn it is, and let them make a move.
        if whose_turn == PLAYER:
            print_board(board)
            index = get_player_move(board)
            board[index] = player_team

        else:
            index = get_computer_move(board, computer_team)
            board[index] = computer_team

        # Check to see if someone won, and end the game if so.
        win_status = check_for_winner(board)
        if win_status != 'keep playing':
            if win_status == 'tie':
                print('-------------------')
                print("It's a tie!")
                print_board(board)
                break
            else:
                print('-------------------')
                print('The {} wins!'.format(whose_turn))
                print_board(board)
                break

        # If we've made it this far, nobody's won yet, so let's get ready for the next turn.
        if whose_turn == PLAYER:
            whose_turn = COMPUTER
        else:
            whose_turn = PLAYER
