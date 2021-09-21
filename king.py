from math import *
def checkredvalidity(board, row, col, row2, col2):
    if (board[row2][col2].piece == "" and abs(row2 - row) == 1 and abs(col2 - col) == 1 and row > row2):
        return True
    if (abs(row2 - row) == 2 and abs(col2 - col) == 2 and row > row2):
        if (board[(row2 + row) / 2][(col2 + col) / 2].piece == "white"):
            return True
    return False

def checkwhitevalidity(board, row, col, row2, col2):
    if(board[row2][col2].piece == "" and abs(row2-row)==1 and abs(col2-col)==1 and row<row2):
        return True
    if(abs(row2-row)==2 and abs(col2-col)==2 and row<row2):
        if(board[(row2+row)/2][(col2+col)/2].piece=="red"):
            return True
    return False

def checkKingValidity(board, row, col, row2, col2):
    color = board[row][col]
    if color == "red":
        if (board[row2][col2].piece == "" and abs(row2 - row) == 1 and abs(col2 - col) == 1):
            return True
        if (abs(row2 - row) == 2 and abs(col2 - col) == 2):
            if (board[(row2 + row) / 2][(col2 + col) / 2].piece == "white"):
                return True
        return False
    elif color == "white":
        if (board[row2][col2].piece == "" and abs(row2 - row) == 1 and abs(col2 - col) == 1):
            return True
        if (abs(row2 - row) == 2 and abs(col2 - col) == 2):
            if (board[(row2 + row) / 2][(col2 + col) / 2].piece == "red"):
                return True
        return False