board = []
board2 = []
attackboard = []
attackboard2 = []
#csillag = ['\x1b[5;30;41m''\x1b[5;30;41m' + "*" + '\x1b[0m']

first_number = 0
import subprocess
import platform
import os

print("Welcome on board!")
playerOne = input('Choose a name for yourself!\n')
playerTwo = input("Player 2's name?\n")
#Creates six 0s in a row and makes 6 of rowes for both board
print(playerOne,"'s turn", sep="")
for x in range(6):
    board.append(["0"] * 6)

for x in range(6):
    board2.append(["0"] * 6)

for x in range(6):
    attackboard.append(["0"] * 6)

for x in range(6):
    attackboard2.append(["0"] * 6)


#Makes it look good for both board
def print_board(board):
    for row in board:
        print((" ~ ",).join(row))

def print_board(board2):
    for row in board2:
        print(("~").join(row))

def print_board(attackboard):
    for row in attackboard:
        print(("~").join(row))

def print_board(attackboard2):
    for row in attackboard2:
        print(("~").join(row))


print_board(board)

#first_number = int(input("Give the x coordinate:"))
#second_number = int(input("Give the y coordinate: "))

def first_player_turn():
    #Checks if first input number is larger then 6
    global first_number
    global second_number
    while True:
        try:
            first_number = int(input("Give the x coordinate:"))
            second_number = int(input("Give the y coordinate: "))
            if first_number <= 6 and second_number <= 5:
                break
            else:
                print("You have type numbers 1-6")
        except ValueError:
            print("You have type numbers 1-6")
            first_player_turn()
    board[first_number-1][second_number-1] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')
    board[first_number-1][second_number] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')
    
            

def second_player_turn():
    
    #Checks if first input number is larger then 6
    while first_number2 <= 6:
        board2[first_number2-1][second_number2-1] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')
        board2[first_number2-1][second_number2] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')
        return first_number2,second_number2
    else:
        try:
            print("Nem jó szám")
            second_player_turn()
        except ValueError:
            print("You have type numbers 1-6")
            second_player_turn()


def fist_player_second_ship():
    first_number = int(input("Place the first part of your second ship(row): "))
    second_number = int(input("Place the second ship of your second ship: "))

    board[first_number-1][second_number-1] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')
    board[first_number][second_number-1] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')
    board[first_number+1][second_number-1] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')

def second_player_second_ship():
    first_number2 = int(input("Place the first part of your second ship(row): "))
    second_number2 = int(input("Place the second ship of your second ship: "))

    board2[first_number2-1][second_number2-1] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')
    board2[first_number2][second_number2-1] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')
    board2[first_number2+1][second_number2-1] = ('\x1b[6;30;42m''\x1b[6;30;42m' + "x" + '\x1b[0m')

def second_turn():
    input("Press Enter to continue...")

def second_player_shoot():
    print(playerTwo, 'turn')
    for turn in range(3):
        turn += 1
        first_guess_row = int(input("Guess a row: "))
        first_guess_column = int(input("Guess a column: "))
        print(first_guess_column)
        if first_number == first_guess_row and second_number == first_guess_column:
            print("Bang!")
            print(playerOne, "board")
            attackboard[first_guess_row-1][first_guess_column-1] = ('\x1b[5;30;41m''\x1b[5;30;41m' + "*" + '\x1b[0m')
            print_board(attackboard)
            if first_number == first_guess_row and second_number == first_guess_column and first_number == first_guess_row and second_number+1 == first_guess_column:
                print('végem')
        
        elif  first_number == first_guess_row and second_number+1 == first_guess_column:
            print(playerOne, "board")
            print("Bang!")
            attackboard[first_guess_row-1][first_guess_column-1] = ('\x1b[5;30;41m''\x1b[5;30;41m' + "*" + '\x1b[0m')
            print_board(attackboard) 
            if first_number == first_guess_row and second_number == first_guess_column and first_number == first_guess_row and second_number+1 == first_guess_column:
                print('végem')
         
        elif turn == 3:
            print('You are out of guesses!')
            break
        
        else:
            print(playerOne, "board")
            attackboard[first_guess_row-1][first_guess_column-1] = ('\x1b[5;30;43m''\x1b[5;30;43m' + "0" + '\x1b[0m')
            print_board(attackboard)  
            print("Miss...")

def first_player_shoot():
    print(playerOne, "turn")
    for turn in range(3):
        turn += 1
        second_guess_row = int(input("Guess a row: "))
        second_guess_column = int(input("Guess a column: "))
        print(second_guess_column)
        if first_number2 == second_guess_row and second_number2 == second_guess_column:
            print("Bang!")
            print(playerTwo, "board")
            attackboard2[second_guess_row-1][second_guess_column-1] = ('\x1b[5;30;41m''\x1b[5;30;41m' + "*" + '\x1b[0m')
            print_board(attackboard2)
            
        elif  first_number2 == second_guess_row and second_number2+1 == second_guess_column:
            print(playerTwo, "board")
            print("Bang!")
            attackboard2[second_guess_row-1][second_guess_column-1] = ('\x1b[5;30;41m''\x1b[5;30;41m' + "*" + '\x1b[0m')
            print_board(attackboard2)
        elif turn == 3:
            print('You are out of guesses!')
        else:
            print(playerTwo, "board")
            attackboard2[second_guess_row-1][second_guess_column-1] = ('\x1b[5;30;43m''\x1b[5;30;43m' + "0" + '\x1b[0m')
            print_board(attackboard2)  
            print("Miss...")


first_player_turn()
#fist_player_second_ship()
print_board(board)
second_turn()
os.system('clear')
print(playerTwo,"'s turn", sep="")
first_number2 = int(input("Give the x coordinate:"))
second_number2 = int(input("Give the y coordinate: "))
second_player_turn()
#second_player_second_ship()
print_board(board2)
second_player_shoot()
#print(attackboard)
if '\x1b[5;30;41m''\x1b[5;30;41m' + "*" + '\x1b[0m' in attackboard:
    print("You win")
first_player_shoot()