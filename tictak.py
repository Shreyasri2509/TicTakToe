def dsiplay_board(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4] + '|'+board[5] + '|'+board[6])
    print('-----')
    print(board[1] + '|'+board[2] + '|'+board[3])

def player_input():
    '''
    OUTPUT={player 1 marker, player 2 marker}
    '''
    marker=''
    #ask player 1 to choose
    while not (marker=='X' and marker=='O'):
        marker= input('player 1, choose x or o').upper()

        if marker=='X':
            return ('X','O')
        else:
            return ('O','X')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    #all rows
    ((board[1]==board[2]==board[3]==mark)and(board[4]==board[5]==board[6]==mark)and(board[7]==board[8]==board[9]==mark))
    #all col
    ((board[7]==board[4]==board[1]==mark)and(board[8]==board[5]==board[2]==mark)and(board[9]==board[6]==board[3]==mark))
    #2 diagonals
    ((board[7]==board[5]==board[3]==mark)and(board[1]==board[5]==board[9]==mark))

import random
def choose_first():
    flip = random.randint(0,1)

    if flip== 0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):
    position1 = 0
    while position1 not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position1):
        position1 = int(input('Choose a position:(1-9)'))
    return position1

def replay():
    choice = input("play again?? enter yes or no")
    return choice == "Yes"

#while loop to keep running the game
print("WELCOME TO TIC TAC TOE")

while True:
    #play the game
    #set (board, who first,choose marker x o)
    the_board=[' ']*10
    player1_marker,player2_marker= player_input()

    turn= choose_first()
    print(turn+' will go first')

    play_game=input('Ready to play?y or n')
    if play_game=='y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            dsiplay_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                dsiplay_board(the_board)
                print('Player 1 won')
                game_on = False
            else:
                if full_board_check(the_board):
                    dsiplay_board(the_board)
                    print('draw game')
                else:
                    turn = 'Player 2'
        else:
            dsiplay_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                dsiplay_board(the_board)
                print('Player 2 won')
                game_on =  False
            else:
                if full_board_check(the_board):
                    dsiplay_board(the_board)
                    print('Draw')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break