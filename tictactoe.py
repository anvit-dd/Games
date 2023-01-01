import random

board = [[1,2,3], 
         [4,5,6],
         [7,8,9]]
running = True
remaining_list = [1,2,3,4,5,6,7,8,9]

def display_board(board):
    print('+-----+------+------+')
    for i in range(0,3):
        print("|     |      |      |")
        print('| ',board[i][0],' |  ',board[i][1],' |  ',board[i][2],' |')
        print("|     |      |      |")
        print('+-----+------+------+')

def enter_move(board):
    global list
#     The function accepts the board's current status, asks the user about their move, 
#     checks the input, and updates the board according to the user's decision.
# input = (input)->check if the input is a num b/w 1-9 -> ignore numbers which are already taken -> find the coords of the given number -> replace that number with O
    if running:
        input_num = int(input("Your Turn: "))
        if input_num in remaining_list:
            for i, x in enumerate(board):
                if input_num in x:
                    board[i][x.index(input_num)] = "O"
                    del remaining_list[remaining_list.index(input_num)]
        else:
            print("Try again!")
            enter_move(board) #Recursive

def computer_Turn(board):
    # The function browses the board and builds a list of all the free squares; 
    random_num = random.choice(remaining_list)
    for r, x in enumerate(board):
        if random_num in x:
            # print("r: ",r )
            # print("x.index(random_num): ", x.index(random_num))
            board[r][x.index(random_num)] = "X"
            del remaining_list[remaining_list.index(random_num)]
            break

def victory_for(board):
  if check_move(board) == True:
    print("You won!")
    return False
  if check_move(board) == False:
    print("You Lost!")
    return False
  if len(remaining_list) == 0:
    print("It's a tie!")
    return False
  return True

def check_move(board):
    #The function checks the computer's and the User move and updates the board.
    for i in range(len(board)):
        #Check Rows
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            return False

        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            return True
        #Check Columns
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            return False

        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            return True
    #Check Diagonals
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return False

    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return True
    
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return False
    
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return True

computer_Turn(board)
display_board(board)
while running:
  enter_move(board)
  computer_Turn(board)
  display_board(board)
  running = victory_for(board)

input("Press Enter to exit")