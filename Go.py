import numpy
board = numpy.full([9, 9], ".")
print(board)
turn_number = 0

choice = ""
player_choice = ""

'''ToDo
XCreate Github Repo
XCreate function for player input logic to reduce duplication
XPrint turn number
    New int variable that increments per loop and prints
SHOULD WE EVEN HAVE RULES NO ONE LIKES RULES I GUES MAYBE WE SHOULD IMPLEMENT RULES
    XWhat are valid places to play
    What are the liberties of adjacent groups
    Function to check whether a group of stones in dead
        Loop that goes through every adjacent space and confirm for liberties with logic
        to iterate to the next space and check liberties if is also your color
    End state check (both players pass)
    Scoring
        Check points for capture
        Check territory claimed per player
        probably print as a result of end state
Add column and row labels to the board

Eventually look for something to track mouse coords for input
'''


#Function for player input logic
def player_input(player_color):
    #Loop to confirm valid input
    need_input = True
    while(need_input):
        if(player_color == "W"):
            print("White's turn")
        else:
            print("Black's turn")
        """
        choice = input("What would you like to your x value to be?  ")
        x = choice
        #Print(choice)
        choice = input("What would you like to your y value to be?  ")
        y = choice
        """
        player_choice = input("What is your move?  Enter values as X,Y: ")
        player_choice_tuple = tuple(map(int, player_choice.split(",")))

        if(board[player_choice_tuple[0]][player_choice_tuple[1]] == "."):
            board[player_choice_tuple[0]][player_choice_tuple[1]] = player_color
            #Flag to set input_needed to false, causing function to repeat and ask for input again
            need_input = False
        else:
            print("That space is taken, choose a free space")

        """
        if(board[int(x)][int(y)] == "."):
            board[int(x)][int(y)] = player_color
            #Flag to set input_needed to false, causing function to repeat and ask for input again
            need_input = False
        else:
            print("That space is taken, choose a free space")
        """
        print(board)



#Function to check liberties of stones on board
#def check_liberties():

#Loop for play/board placement
while choice != "exit":
    turn_number = turn_number + 1
    print("Turn: " + str(turn_number))
#First player loop for coordinates
    player_input("B")
#Second player loop for coordinates
    player_input("W")

