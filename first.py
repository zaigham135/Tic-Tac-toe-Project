# def user_input():
#     user1 = "wrong"
#     user2 = "wrong"
#     while user1 and user2 not in ['o', 'x']:
#         user1 = input("user1: Enter x or o:  ")
#         if user1 == "x":
#             user2 = input("user2: Enter  o: ")
#         elif user1 != "x" and user1 != "o":
#             print("please write correct input: either x or o.")
#         else:
#             user2 = input("user2: Enter x: ")
#
#     return user1, user2


def display_board(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-------------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] )
    print("-------------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] )


def player_input():
    marker = " "
    while marker != 'x' and marker != 'o':
        marker = input("player 1: Do you want to be x or o? :  ")
        if marker == 'x':
            return ('x', 'o')
        else:
            return ('o', 'x')


# board = [" "] * 10
#
#
def place_marker(board, marker, position):
    board[position] = marker
#
#
# print(place_marker(board, "x", 5))
# print(display_board(board))


def win_check(board, marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker))


# print(win_check(board, 'x'))

import random


def choose_first():
    if random.randint(0, 1) == 0:
        return "player 2"
    else:
        return "player 1"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose your position (1-9): "))
    return position


def replay():
    return input("Do you want to play again? Enter yes or no: ").startswith("y")


print("Welcome to the Tic Tac Toe game.")

while True:
    boardd = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    play_game = input("Are you ready to play the game: Enter yes or no: ")
    if play_game == "yes":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "player 1":
            display_board(boardd)
            position = player_choice(boardd)
            place_marker(boardd, player1_marker, position)
            if win_check(boardd, player1_marker):
                display_board(boardd)
                print("player 1 won the game")
                game_on = False
            else:
                if full_board_check(boardd):
                    display_board(boardd)
                    print("The match draw!")
                    break
                else:
                    turn = "player 2"


        else:
            display_board(boardd)
            position = player_choice(boardd)
            place_marker(boardd, player2_marker, position)
            if win_check(boardd, player2_marker):
                display_board(boardd)
                print("player 2 won the match!!")
                game_on = False
            else:
                if full_board_check(boardd):
                    display_board(boardd)
                    print("The match is Draw!")
                    break
                else:
                    turn = "player 1"

    if not replay():
        break
