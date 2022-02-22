#Step 1 Print out a board
#from IPython.display import clear_output -only works in jupyter

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


test_board = ['X','X','X','X','X','O','X','X',' ','X']
display_board(test_board)

#Step 2 Asking for user input to assign them with a marker: X or O

def player_choice():
    '''
    Output (Player 1, Player 2)
    '''

    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input('Player1 choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')

    if marker == 'O':
        return ('O', 'X')

player_choice()


#Step 3  Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board,marker,position):
    board[position] = marker

place_marker(test_board,'O',4)
display_board(test_board)



#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

def win_check(board, mark):
    '''
    Checking if the player has won or not by checking all rows, columns and both diaganols.
    '''

    #check rows
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    #check columns
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    #check diagnols
    (board[7] == board[5] == board[3] == mark) or
    (board[1] == board[5] == board[9] == mark))

win_check(test_board,'X')

#Step 5: Write a function that uses the random module to randomly decide which player goes first. Return a string of
#which player went first.

import random

def choose_first():
    ''' Randomly assigns which player will go first.
    '''
    players = ['Player 1', 'Player 2']

    results = random.choices(players, k=1)
    print(results)
choose_first()

#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):

    if board[position] == ' ':
        print(f'True')
    else:
        print(f'False')

space_check(test_board,4)

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step
# 6 to check if it's a free position. If it is, then return the position for later use.
def player_position(board):

    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input(f'Choose your next position, 1-9? '))

    return position

player_position(test_board)

#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to
# play again.

def replay():
    choice = input(f'Would you like to play again? Y or N: ')

    return choice == 'Yes'

replay()


#WHILE LOOPS TO KEEP THE GAME RUNNING
print(f'Welcome to Tic Tac Toe!')

while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_choice()
    turn = choose_first()
    print(turn + 'will go first')

    play_game = input('Ready to play? y or n ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

##GAME PLAY
    while game_on:
        if turn == 'Player 1':

        # Show the board
            display_board(the_board)

        #Choose the position
            position = player_position(the_board)

        #Place the marker on the position
            place_marker(the_board,player1_marker,position)

        #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print(f'PLAYER 1 HAS WON!')
                game_on = False

        # Or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print(f'Tie game!')
                    game_on = False

                else:
                    turn = 'Player 2'

    else:



        display_board(the_board)
        position = player_position(the_board)
        place_marker(the_board, player1_marker, position)

        # Check if they won
        if win_check(the_board, player1_marker):
            display_board(the_board)
            print(f'PLAYER 1 HAS WON!')
            game_on = False

        # Or check if there is a tie
        else:
            if full_board_check(the_board):
                display_board(the_board)
                print(f'Tie game!')
                game_on = False

            else:
                turn = 'Player 2'
    if not replay():
        break