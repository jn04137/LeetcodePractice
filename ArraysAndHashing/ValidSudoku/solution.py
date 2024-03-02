
# Valid Sudoku
'''
General notes, got the check for rows and columns pretty easily with 
the help of python's dictionaries.

Was failing to understand how to solve the number in each square. 
Able to use the division and floor operator to figure out which
square the value falls in. Helper method returns the coord as a
string to be passed into a hashmap as a key. Value contains a set
with values that are already stored.
'''

from typing import List

'''
Two Hashmaps
- one for x-coords
- one for y-coords

Each value will be a list of integers that already existing on each
row/column

Would probably be better to use a set here
'''

#board: List[List[str]] = [
#        ["5","3",".",".","7",".",".",".","."],
#        ["6",".",".","1","9","5",".",".","."],
#        [".","9","8",".",".",".",".","6","."],
#        ["8",".",".",".","6",".",".",".","3"],
#        ["4",".",".","8",".","3",".",".","1"],
#        ["7",".",".",".","2",".",".",".","6"],
#        [".","6",".",".",".",".","2","8","."],
#        [".",".",".","4","1","9",".",".","5"],
#        [".",".",".",".","8",".",".","7","9"]]

board = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]

'''
Maybe I just create a helper method to figure out which block the 
value belongs to.

Had to take a slight peek at the solution. Need to use the floor operator after division
'''

def getSquareCoord(coords) -> str :
   
    x_block = coords[0] // 3
    y_block = coords[1] // 3
    return str(x_block) + "," + str(y_block)

def isValidSudoku(board: List[List[str]]) -> bool:
    x_coords = {}
    y_coords = {}
    squares = {}

    for x in range(9):
        x_coords[x] = set()
        y_coords[x] = set()

    for i in range(3):
        for y in range(3):
            squares[str(i)+","+str(y)]=set()

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == ".":
                continue
            elif (board[row][column] in x_coords[column] or 
                  board[row][column] in y_coords[row] or
                  board[row][column] in squares[getSquareCoord([row, column])]):
                return False
            else:
                x_coords[column].add(board[row][column])
                y_coords[row].add(board[row][column])
                squares[getSquareCoord([row, column])].add(board[row][column])

    return True 

print(isValidSudoku(board))

