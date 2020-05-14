from os import system

def print_Numbers():
    print()
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    print()
	
def print_Board(myBoard):
    print()
    print(f"{myBoard[0]} | {myBoard[1]} | {myBoard[2]}")
    print(f"{myBoard[3]} | {myBoard[4]} | {myBoard[5]}")
    print(f"{myBoard[6]} | {myBoard[7]} | {myBoard[8]}")
    print()

def is_complete(myBoard):
    # Rows
    if (myBoard[0] == myBoard[1] == myBoard[2] != ' '): return True
    if (myBoard[3] == myBoard[4] == myBoard[5] != ' '): return True
    if (myBoard[6] == myBoard[7] == myBoard[8] != ' '): return True
    # Columns
    if (myBoard[0] == myBoard[3] == myBoard[6] != ' '): return True
    if (myBoard[1] == myBoard[4] == myBoard[7] != ' '): return True
    if (myBoard[2] == myBoard[5] == myBoard[8] != ' '): return True
    # Diagonals
    if (myBoard[0] == myBoard[4] == myBoard[8] != ' '): return True
    if (myBoard[2] == myBoard[4] == myBoard[6] != ' '): return True
    return False

def is_full(myBoard):
    if (not is_complete(myBoard)):
        for char in myBoard:
            if (char == ' '):
                return False
    return True

player1_sym = ''
player2_sym = ''
while(player1_sym != 'X' and player1_sym != 'O'):
    player1_sym = input("Choose player 1 symbol: 'X' or 'O': ")
if (player1_sym == 'X'): player2_sym = 'O'
else: player2_sym = 'X'

print(f"Player 1 Symbol = {player1_sym}")
print(f"Player 2 Symbol = {player2_sym}")

myBoard = list(' ' * 9)
is_player1_turn = True
is_player2_turn = False

while(not is_complete(myBoard)):

    if (is_full(myBoard)):
        is_player1_turn = is_player2_turn = False
        break

    print_Board(myBoard)
    print_Numbers()

    # Take input
    if (is_player1_turn):
        print("Player 1's turn")
        move = 10
        while (move not in range(0, 9)): move = int(input("Enter the position number: "))
        while(myBoard[move] != ' '):
            if(myBoard[move] != ' '): move = 10
            while(move not in range(0, 9)):
                print("Player 1's turn")
                move = int(input("Enter the position number: "))
        myBoard[move] = player1_sym
        is_player2_turn = True
        is_player1_turn = False

    elif (is_player2_turn):
        print("Player 2's turn")
        move = 10
        while (move not in range(0, 9)): move = int(input("Enter the position number: "))
        while (myBoard[move] != ' '):
            if (myBoard[move] != ' '): move = 10
            while (move not in range(0, 9)):
                print("Player 2's turn")
                move = int(input("Enter the position number: "))
        myBoard[move] = player2_sym
        is_player2_turn = False
        is_player1_turn = True
    #print("\n" * 100)
    system("cls")

# Win message
print_Board(myBoard)
if((not is_player2_turn) and (not is_player1_turn)):
    print(f"GAME TIED!")
elif(not is_player1_turn):
    print(f"Player 1 won the GAME.")
elif (not is_player2_turn):
    print(f"Player 2 won the GAME.")