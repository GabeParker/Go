import numpy
board = numpy.full([9, 9], ".")
print(board)

choice = ""

'''ToDo
Create function for player input logice to reduce duplication
Print turn number
	New int variable that increments per loop and prints
SHOULD WE EVEN HAVE RULES NO ONE LIKES RULES I GUES MAYBE WE SHOULD IMPLEMENT RULES
	What are valid places to play
	What are the liberties of adjacent groups
	Function to check whether a group of stones in dead
		Loop that goes through every adjacent space and confirm for liberties with logic
		to iterate to the next space and check liberties if is also your color
	End state check (both players pass)
	Scoring
		Check points for capture
		Check territory claimed per player
		probably print as a result of end state
'''


#Loop for play/board placement
while choice != "exit":
#First player loop for coordinates
    choice = input("What would you like to your x value to be?  ")
    x = choice
    #print(choice)
    choice = input("What would you like to your y value to be?  ")
    y = choice
    if(board[int(x)][int(y)] == "."):
    	board[int(x)][int(y)] = "w"
    print(board)

#Second player loop for coordinates
    choice = input("What would you like to your x value to be?  ")
    x = choice
    #print(choice)
    choice = input("What would you like to your y value to be?  ")
    y = choice
    if(board[int(x)][int(y)] == "."):
    	board[int(x)][int(y)] = "b"
    print(board)