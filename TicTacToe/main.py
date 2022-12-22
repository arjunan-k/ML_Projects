# -------------------------------------------------------------------------------- #
from logo import LOGO               # Importing modules.

a = 0                               # Importing global variables.
PLAYER1_SCORE = 0
PLAYER2_SCORE = 0


def print_scoreboard():             # To print the scoreboard.

    print("------------------------------")
    print("          SCOREBOARD          ")
    print("------------------------------")
    print(f"{PLAYER1} ---> {PLAYER1_SCORE}")
    print(f"{PLAYER2} ---> {PLAYER2_SCORE}")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def tictactoe_board():              # To print the play table.

    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}\n"
          f"_________________\n"
          f"  {board[3]}  |  {board[4]}  |  {board[5]}\n"
          f"_________________\n"
          f"  {board[6]}  |  {board[7]}  |  {board[8]}\n")

SOLUTIONS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def check_game_over(player):        # To check the answer.

    for element in SOLUTIONS:
        if board[element[0]] == board[element[1]] == board[element[2]] == player:
            return True


def short_name(name):               # To make input name short to 3 letters.

    c = []
    b = ""
    for element in name:
        c.append(element)
    for each in range(3):
        b += c[each]
    return b


def second_box():                   # To make the second player movement.

    box2 = input(f"Hlo {PLAYER2}, which box from 1-9 to place {PLAYER2_DICE}?: ")
    board[int(box2) - 1] = PLAYER2_DICE
    if check_game_over(PLAYER2_DICE):
        global PLAYER2_SCORE
        PLAYER2_SCORE += 1
        print(f"{PLAYER2} is the Winner")
        tictactoe_board()
        print_scoreboard()
        return True


def playing_game():                 # To play the dice until game over.

    global a
    while a < 9:
        tictactoe_board()
        box1 = input(f"Hlo {PLAYER1}, which box from 1-9 to place {PLAYER1_DICE}?: ")
        board[int(box1) - 1] = PLAYER1_DICE
        tictactoe_board()
        if check_game_over(PLAYER1_DICE):
            global PLAYER1_SCORE
            PLAYER1_SCORE += 1
            print(f"{PLAYER1} is the Winner")
            print_scoreboard()
            return True
        else:
            a += 1
            if a >= 9:
                print("Its a Draw, Both are Winners.")
                return True
            if second_box():
                return True
            else:
                a += 1
                if a >= 9:
                    print("Its a Draw, Both are Winners.")
                    return True


is_on = True                        # Starting the game.
while is_on:

    print(LOGO)
    print("Player 1")
    PLAYER1 = input("Enter the name: ").title()
    PLAYER1 = short_name(PLAYER1)
    print("\nPlayer 2")
    PLAYER2 = input("Enter the name: ").title()
    PLAYER2 = short_name(PLAYER2)
    print_scoreboard()
    print(f"\nTurn to choose for {PLAYER1}")
    CHOICE = input("Enter 1 for X\nEnter 2 for 0\nEnter 3 to Quit\n").lower()

    if CHOICE == "1":
        PLAYER1_DICE = "X"
        PLAYER2_DICE = "O"
        if playing_game():
            is_on = False

    elif CHOICE == "2":
        PLAYER1_DICE = "O"
        PLAYER2_DICE = "X"
        if playing_game():
            is_on = False

    elif CHOICE == "3":
        print("Final Scoreboard")
        print_scoreboard()
        is_on = False

    else:
        print("Wrong Input!!! Try Again")
        is_on = False
# -------------------------------------------------------------------------------- #