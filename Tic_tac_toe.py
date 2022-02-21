#Print out a board
#from IPython.display import clear_output -only works in jupyter

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)

#Asking for user input to assign them with a marker: X or O

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
#Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board,marker,position):
    board[position] = marker

place_marker(test_board,'X',3)
display_board(test_board)

#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
#ALL ROWS check if they share the same marker.
#ALL COLUMNS check if they share the same marker.
#2 diagonals check if they share the same marker.
def win_check(board, mark):
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

display_board(test_board)
win_check(test_board,'X')
