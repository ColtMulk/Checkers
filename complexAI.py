from validmove import *
from random import randint

def findRedMoves(board):
    """
        Finds all the moves and returns a move for the computer to make
        based on the smartest move of the set
    :param board:
    :return: Returns the move in the form of row, col, row2, col2
    """
    score = []
    redlist = []
    for row in range(8):
        for col in range(8):
            if board[row][col].piece == 'red':
                redlist.append([row, col])
    moves = []
    for i in range(len(redlist)):
        row = redlist[i][0]
        col = redlist[i][1]
        if (board[row][col].piece == "red"):
            if (checkredvalidity(board, row, col, row - 1, col - 1)):
                moves.append([row, col, row - 1, col - 1])
                score.append(0)
            if (checkredvalidity(board, row, col, row - 1, col + 1)):
                moves.append([row, col, row - 1, col + 1])
                score.append(0)
            if (checkredvalidity(board, row, col, row - 2, col - 2)):
                moves.append([row, col, row - 2, col - 2])
                score.append(10)
            if (checkredvalidity(board, row, col, row - 2, col + 2)):
                moves.append([row, col, row - 2, col - 2])
                score.append(10)
            if (board[row][col].king):
                if (checkKingValidity(board, row, col, row - 1, col - 1, 'red')):
                    moves.append([row, col, row - 1, col - 1])
                    score.append(0)
                if (checkKingValidity(board, row, col, row - 1, col + 1, 'red')):
                    moves.append([row, col, row - 1, col + 1])
                    score.append(0)
                if (checkKingValidity(board, row, col, row + 1, col - 1, 'red')):
                    moves.append([row, col, row + 1, col - 1])
                if (checkKingValidity(board, row, col, row + 1, col + 1, 'red')):
                    moves.append([row, col, row + 1, col + 1])
                    score.append(0)
                if (checkKingValidity(board, row, col, row - 2, col - 2, 'red')):
                    moves.append([row, col, row - 2, col - 2])
                    score.append(10)
                if (checkKingValidity(board, row, col, row - 2, col + 2, 'red')):
                    moves.append([row, col, row - 2, col + 2])
                    score.append(10)
                if (checkKingValidity(board, row, col, row + 2, col - 2, 'red')):
                    moves.append([row, col, row + 2, col - 2])
                    score.append(10)
                if (checkKingValidity(board, row, col, row + 2, col + 2, 'red')):
                    moves.append([row, col, row + 2, col + 2])
                    score.append(10)
    bestmoves = []
    for i in range(len(score)):
        for j in range(len(score)):
            if(score[i]>score[j]):
                temp = score[i]
                tempmove = moves[i]
                score[i] = score[j]
                moves[i] = moves[j]
                score[j] = temp
                moves[j] = tempmove

    if 10 in score:
        for i in range(len(score)):
            if(score[i]==10):
                bestmoves.append(moves[i])
        index = randint(0,len(bestmoves)-1)
        return(bestmoves[index][0], bestmoves[index][1], bestmoves[index][2], bestmoves[index][3])
    else:
        index = randint(0, len(moves) - 1)
        return (moves[index][0], moves[index][1], moves[index][2], moves[index][3])