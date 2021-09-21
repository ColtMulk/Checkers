from math import *
def checkredvalidity(board, row, col, row2, col2):
    """takes in row and col of piece selected and where its headed
        returns if its a valid move for red piece"""

    color = board[row][col].piece
    #checks if its the right color piece
    if(color != 'red'):
        return False


    # checks if out of bounds
    if(row<0 or row2 <0 or row >7 or row2 > 7 or col<0 or col2<0 or col>7 or col2 >7):
        return False
    if (board[row2][col2].piece != ""):
        return False
    #chceks for diaganol move
    if (board[row2][col2].piece == "" and (row2 == row-1 and abs(col2-col)== 1)):
        return True
    #checks for jump move
    if (abs(row2 - row) == 2 and abs(col2 - col) == 2 and row > row2):
        nrow = max(row2, row) - 1
        ncol = max(col2, col) - 1
        if(board[row2][col2].piece != ""):
            return False
        if (board[nrow][ncol].piece == "white"):
            return True
    return False

def checkwhitevalidity(board, row, col, row2, col2):
    """takes in row and col of piece selected and where its headed
        returns if its a valid move for white piece"""
    color = board[row][col].piece
    # checks if its the right color piece
    if (color != 'white'):
        return False
    if(board[row2][col2].piece != ""):
        return False
    # checks if out of bounds

    if (row < 0 or row2 < 0 or row > 7 or row2 > 7 or col < 0 or col2 < 0 or col > 7 or col2 > 7):
        return False
    #checks for diagonal move
    if(board[row2][col2].piece == "" and (row2 == row+1 and abs(col2-col)==1)):
        return True
    #checks for jump
    if(abs(row2-row)==2 and abs(col2-col)==2 and row<row2):
        nrow = max(row2,row)-1
        ncol = max(col2,col)-1
        if (board[row2][col2].piece != ""):
            return False
        if(board[nrow][ncol].piece=="red"):
            return True
    return False

def checkKingValidity(board, row, col, row2, col2, turn):
    """takes in row and col of piece selected and where its headed
    returns if its a valid move for a king piece
    turn is the color of whose turn it is either "white" or "red" """
    # cheks if out of bounds
    if (row < 0 or row2 < 0 or row > 7 or row2 > 7 or col < 0 or col2 < 0 or col > 7 or col2 > 7):
        return False
    color = board[row][col].piece
    #checks if its the right king
    if(turn != color):
        return False
    #checks for color
    if color == "red":
        #checks diaganol move
        if (board[row2][col2].piece == "" and abs(row2 - row) == 1 and abs(col2 - col) == 1):
            return True
        #checks jump move
        if (abs(row2 - row) == 2 and abs(col2 - col) == 2):
            nrow = max(row2, row) - 1
            ncol = max(col2, col) - 1
            if (board[row2][col2].piece != ""):
                return False
            if (board[nrow][ncol].piece == "white"):
                return True
        return False

    if color == "white":
        #checks diaganol move
        if (board[row2][col2].piece == "" and abs(row2 - row) == 1 and abs(col2 - col) == 1):
            return True
        #checks jump move
        if (abs(row2 - row) == 2 and abs(col2 - col) == 2):
            nrow= max(row2,row)-1
            ncol = max(col2,col)-1
            if (board[row2][col2].piece != ""):
                return False
            if (board[nrow][ncol].piece == "red"):
                return True
        return False


