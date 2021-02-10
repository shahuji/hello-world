# import random

# Welcome to Tic-Tac_toe game...
the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in the_board:
    board_keys.append(key)


def printBoard(board_pr):
    print(board_pr['7'] + '|' + board_pr['8'] + '|' + board_pr['9'])
    print('-+-+-')
    print(board_pr['4'] + '|' + board_pr['5'] + '|' + board_pr['6'])
    print('-+-+-')
    print(board_pr['1'] + '|' + board_pr['2'] + '|' + board_pr['3'])


def game():

    print("Welcome to Tic-Tac-Toe game...")
    turn = 'X'
    count = 0

    for i in range(1, 10):
        print('--- ', i, ' ---')

        # if i%2 == 0:
        #     move = str(random.randint(1, 9))
        #     if the_board[move] == ' ':
        #         print("It's turn " + turn + ". ")
        #         the_board[move] = turn
        #         count += 1
        #     else:
        #         continue
        #
        # else:
        print("It's your turn " + turn + ". Which place you want to write?  ")

        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("Place is already field. \nMove to which place?")
            continue

        printBoard(the_board)

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9']:
                printBoard(the_board)
                print('-!-  Game Over -!-')
                print("*** " + turn + " won ***")
                break

            elif the_board['4'] == the_board['5'] == the_board['6']:
                printBoard(the_board)
                print('-!-  Game Over -!-')
                print("*** " + turn + " won ***")
                break

            elif the_board['1'] == the_board['2'] == the_board['3']:
                printBoard(the_board)
                print('-!-  Game Over -!-')
                print("*** " + turn + " won ***")
                break

            elif the_board['1'] == the_board['4'] == the_board['7']:
                printBoard(the_board)
                print('-!-  Game Over -!-')
                print("*** " + turn + " won ***")
                break

            elif the_board['2'] == the_board['5'] == the_board['8']:
                printBoard(the_board)
                print('-!-  Game Over -!-')
                print("*** " + turn + " won ***")
                break

            elif the_board['3'] == the_board['6'] == the_board['9']:
                printBoard(the_board)
                print('-!-  Game Over -!-')
                print("*** " + turn + " won ***")
                break

            elif the_board['1'] == the_board['5'] == the_board['9']:
                printBoard(the_board)
                print('-!-  Game Over -!-')
                print("*** " + turn + " won ***")
                break

            elif the_board['7'] == the_board['5'] == the_board['3']:
                printBoard(the_board)
                print('-!-  Game Over -!-')
                print("*** " + turn + " won ***")
                break

        if count == 9:
            print('\n\t*-!-* Game Over *-!-*\n')
            print("\tIt's a tie")

        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

    restart = input("Do want to play agian?(y/n) ")
    if restart == 'y' or restart == 'Y':
        for keys in board_keys:
            the_board[keys] = ' '

        game()


if __name__ == '__main__':
    game()

