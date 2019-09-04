# A python program to play Tic Tac Toe for 2 players.

# A function to print the board.
def game_board(board):
    print( ' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print( ' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print( ' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

# Adding the characters in the desired positions.
def player_X_turn(position):
    dummy_board[position] = "X"

def player_O_turn(position):
    dummy_board[position] = "O"

# Checking coniditions if a winning patern has been provided.
def check_win(play):
    for i in range(0,3):
        j=i*3
        # Row check
        if (play[j] == play[j+1] and play[j] == play[j+2]):
            print("\nRow win")
            return True
        # Column check
        elif (play[i] == play[i+3] and play[i] == play[i+6]):
            print("\nColumn win")
            return  True
        # Diagonal check
        elif ((play[0] == play[4] and play[0] == play[8] ) or (play[2] == play[4] and play[2] == play[6])):
            print("\nDiagonal win")
            return True

# The main place where the action happens.
# An infinite loop if the users are very competitive with each other, so the game goes on and on.
while True:
    # A dummy board for user reference.
    dummy_board = []
    for i in range(9):
        dummy_board.append(str(i))
    # Variable used for checking draw condition
    count = 0
    print("\nLet the game begin!\n")
    # The game execution loop, one game at a time.
    while(count<=8):
        game_board(dummy_board)
        player_X_turn(int(input("\nPlayer X enter your position : ")))
        if check_win(dummy_board):
            print("Player X wins the game")
            game_board(dummy_board)
            break
        count+=1
        if (count == 9):
            print("Match Draw")
            break
        game_board(dummy_board)
        player_O_turn(int(input("\nPlayer O enter your position : ")))
        if check_win(dummy_board):
            print("Player O wins the game")
            game_board(dummy_board)
            break
        count += 1
    if not(input("\nPlay Again? Yes or No ").lower().startswith("y")):
        break

