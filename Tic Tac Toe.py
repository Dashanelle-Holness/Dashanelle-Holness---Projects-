import random

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentplayer = "X"
winner = None
gameRunning = True

# Taking players input
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Check for the win or tie
def checkWin():
    global gameRunning
    global winner
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            winner = board[i]
            gameRunning = False
            return

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            winner = board[i]
            gameRunning = False
            return

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        gameRunning = False
        return
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        gameRunning = False
        return

    # Check for a tie
    if "-" not in board:
        winner = None
        gameRunning = False

def playerInput():
    global currentplayer
    position = int(input("Enter a number 1-9: ")) - 1
    if position >= 0 and position < 9 and board[position] == "-":
        board[position] = currentplayer
    else:
        print("Oops player is already in that spot !")
        playerInput()

def switchPlayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

# Check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput()
    checkWin()
    switchPlayer()

# Print the final board and winner/tie
printBoard(board)
if winner:
    print(f"The winner is {winner}!")
else:
    print("It's a tie!")
