# To print out a board.

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# write a function to display the board.

def print_board(board): 
    for i in range(len(board)): # Iterate through the length of the board i.e through the num of lists
        if i % 3 == 0 and i != 0: # Divides the board on the 4th row.
            print("- - - - - - - - - - - - - ")
        
        for j in range(len(board[0])): # Iterate through the length of the list element.
            if j % 3 == 0 and j != 0: # Divides the board on the 4th column
                print('| ', end='')

            if j == 8: # Checks if its the last element of the puzzle and prints it
                print(board[i][j])
            else: # converts the elements of the list to a string and prints them.
                print(str(board[i][j]) + " ", end='')
    return None

def find_empty(board): # Iterates through the rows and columns of the board to find the Zero's and return its index.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
        
    return None

def is_valid(board, row, column, input_num):
    # Checks Row
    for element in range(len(board[row])):
        if board[row][element] == input_num:
            return False
    
    # Checks Column
    for rows in range(len(board)):
        if board[rows][column] == input_num:
            return False

    # Check inner-square
    row = row - (row % 3)
    column = column - (column % 3)
    for i in range(3):
        for j in range(3):
            if board[row + i][column + j] == input_num:
                return False

    return True

def solve_sudoku(board):
    if not find_empty(board):
        return True 

    else:
        x, y = find_empty(board)
    for i in range(1, 10):
        if is_valid(board, x, y, i):
            board[x][y] = i 
            print(board[x][y])

            if solve_sudoku(board):
                return True

            board[x][y] = 0

    return False
           

solve_sudoku(board)
print_board(board)
