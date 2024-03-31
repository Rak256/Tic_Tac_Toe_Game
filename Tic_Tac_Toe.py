row1 = ["*", "*", "*"]
row2 = ["*", "*", "*"]
row3 = ["*", "*", "*"]
player1 = [True]

# display board
def display_board (row1, row2, row3):
    print (row1)
    print (row2)
    print (row3)

#Take input
def player_choice(row1, row2, row3):

    valid = False
    choice = ["Wrong", "Wrong"]

    loop = True
    while(loop or not valid):
        in1 = input("Please enter the row you want to mark in (starts from 0): ")
        in2 = input("Please enter the column you want to mark in (starts from 0): ")
        choice[0] = in1
        choice[1] = in2
        for index, value in enumerate(choice):
            if not value.isdigit():
                print(f"Sorry! Input {index} is not a number")
                break
            else:
                choice[index] = int(value)
                if int (value) not in [0,1,2]:
                    print (f"Sorry! Input {index} is not a number in the list [0,1,2]")
                    break
                else:
                    loop = False
        choice[0] = int(in1)
        choice[1] = int(in2)
        
        
        if choice[0] == 0:
            if not (row1[choice[1]] == "X" or row1[choice[1]] == "O"):
                valid = True
            else:
                print("Sorry that spot is already marked!")
        elif choice[0] == 1:
            if not (row2[choice[1]] == "X" or row2[choice[1]] == "O"):
                valid = True
            else:
                print("Sorry that spot is already marked!")
        else:
            if not (row3[choice[1]] == "X" or row3[choice[1]] == "O"):
                valid = True
            else:
                print("Sorry that spot is already marked!")

    return choice

#Manipulate board
def Change_board(player_choice, row1, row2, row3):
    global player1

    if player1[0]:

        if player_choice[0] == 0:
            row1[player_choice[1]] = "X"
        
        elif player_choice[0] == 1:
            row2[player_choice[1]] = "X"

        else:
            row3[player_choice[1]] = "X"
    
    else:
        if player_choice[0] == 0:
            row1[player_choice[1]] = "O"
        
        elif player_choice[0] == 1:
            row2[player_choice[1]] = "O"

        else:
            row3[player_choice[1]] = "O"

    player1[0] = not player1[0]

#Win_condition
def Won(row1, row2, row3):
    if (row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X') or (row1[0] == 'X' and row1[1] == 'X' and row1[2] == 'X') or (row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X') or (row3[0] == 'X' and row3[1] == 'X' and row3[2] == 'X') or (row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X') or (row1[1]== 'X' and row2[1] == 'X' and row3[1] == 'X') or (row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X') or (row1[2] == 'X' and row2[1] == 'X' and row3[0] == 'X'):
        print('Player 1 Won!')
        return True
    elif (row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O') or (row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O') or (row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O') or (row3[0] == 'O' and row3[1] == 'O' and row3[2] == 'O') or (row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O') or (row1[1]== 'O' and row2[1] == 'O' and row3[1] == 'O') or (row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O') or (row1[2] == 'O' and row2[1] == 'O' and row3[0] == 'O'):
        print('Player 2 Won')
        return True
    elif all(row1[index] != "*" for index in [0,1,2]) and all(row2[index] != "*" for index in [0,1,2]) and all(row3[index] != "*" for index in [0,1,2]):
        print("The game is a draw!")
        return True
    else:
        return False

#Make Game loop
def Tic_Tac_Toe(row1,row2,row3):
    while(not Won(row1,row2,row3)):
        display_board(row1,row2,row3)
        Change_board(player_choice(row1, row2, row3), row1, row2, row3)

Tic_Tac_Toe(row1, row2, row3)