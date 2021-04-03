# --------- Global Variables --------- #

# Game board
board = ["-", "-","-",
         "-","-","-",
         "-","-","-"]

game_still_going = True

# Who's turn is it?
current_player = "X"

# Who won? or tie?(if somebody wins we'll change the value from None to 'X' or 'O' else we'll keep None)
winner = None


# Displaying initial board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Main function to run the game
def play_game():

    #added some comment for github issue for practicing
    #Added another commnet to check branching
    #Okay one more time
    #let's see again

    # setting up global variable
    global winner

    # display the initial board
    display_board()

    # Keeping the game going until someone Wins or Tie
    while game_still_going:
        # handle a single turn of an arbitrary player(the argument is for checking which player is handling a turn)
        handle_turn(current_player)

        # Checking if the game is over (someone wins or tie)
        check_if_game_over()

        """
        to flip the player ('X' <-> 'O')( assuming the game is not over yet ) 
        after fliping the player it will go back to the start again until 
        someone have his pieces 3 in a row/column/diagonal or tie and then the loop will break 
        """
        flip_player()

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won')
    elif winner == None:
        print("It's a tie")

# function for handling a single turn of an arbitrary player
def handle_turn(player):
    # Setting up global Variable
    global board

    # check who's turn is it
    print(player + "'s turn.")

    # taking position from the user
    position = input("Choose a position from 1-9: ")
    
    # If any arbitrary user tries to use the position which is already used up, it will ask again
    valid = False
    while not valid:

        # If the input is invalid it will ask again
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print("You can't go there, Go again")

    # taking a postion at the board 
    board[position] = player
    # Displaying the board with occupied position
    display_board()

# function to check if the game is over(someone wins or tie)
def check_if_game_over():
    # here we have to check whether someone wins or there is a tie
    check_for_winner()
    check_if_tie()

# Checking if there is a win
def check_for_winner():
    # setting up global variable
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #There is no win
        winner = None
    pass

# The function will check for a match of 3 same pieces in a row
def check_rows():
    # setting up the global variable
    global game_still_going

    # Check any of the rows have all the same value and (is not empty)
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    # If any row does have a match, flag that there is a win(Game loop will break)
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner (X or O)    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    

# Will check for a match of 3 same pieces in a column
def check_columns():
    # setting up the global variable
    global game_still_going

    # Check any of the columns have all the same value and (is not empty)
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    # If any column does have a match, flag that there is a win(Game loop will break)
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


# will check for a match of 3 same pieces in a diagonal
def check_diagonals():
    # setting up the global variable
    global game_still_going

    # Check any of the diagonals have all the same value and (is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'
    
    # If any diagonal does have a match, flag that there is a win(Game loop will break)
    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]


# checking if there is a tie
def check_if_tie():
    # set up global variable
    global game_still_going

    if '-' not in board:
        game_still_going = False

    pass

# function for flipping the player from 'X' <> 'O' ( so that we know which piece('X' or 'O') to place in the postion )
def flip_player():
    # Set up global variable
    global current_player

    # If the current player is 'X' then change it to 'O'
    if current_player == 'X':
        current_player = 'O'
    # If the current player is 'O', change it to 'X'    
    elif current_player == 'O':
        current_player = 'X'
    pass





# ----------------- BEGIN THE GAME -------------------- # 

# Calling the main function to start the game #
play_game()

# ------------------------------------------------------#


"""
# We're going to need these to build up the game
# Board
# display board
# play game
# handle turn
# check win
    # check rows
    # check collumns
    # check diagonals
# check tie
# flip player
"""
