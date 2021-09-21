from copy import deepcopy

def is_won(board):
    """
        Returns true if the game has been won
    """
    return board.gameWon != board.NOTDONE

def minMax(board):
    bestBoard = None
    currentDepth = board.depth + 1
    while not bestBoard and currentDepth > 0:
        currentDepth -= 1
        (bestBoard, bestVal) = maxMove(board, currentDepth)
    if not bestBoard:
        raise Exception("Could only return null boards")
    else:
        return (bestBoard, bestVal)

def maxMove(maxBoard, currentDepth):
    return maxMinBoard(maxBoard, currentDepth-1, float('-inf'))

def minMove(minBoard, currentDepth):
    return maxMinBoard(minBoard, currentDepth-1, float('inf'))

def maxMinBoard(board, currentDepth, bestMove, redcounter, whitecounter):
    if whitecounter == 0 or redcounter == 0 or currentDepth <= 0:
        return (board, staticEval(board))
    best_move = bestMove
    best_board = None

    if bestMove == float('-inf'):
        moves = board.iterRedMoves()
        for move in moves:
            maxBoard = deepcopy(board)
            maxBoard.moveSilentRed(*move)
            value = minMove(maxBoard, currentDepth-1)[1]
            if value > best_move:
                best_move = value
                best_board = maxBoard

    elif bestMove == float('inf'):
        moves = board.iterWhiteMoves()
        for move in moves:
            minBoard = deepcopy(board)
            minBoard.moveSilentWhite(*move)
            value = maxMove(minBoard, currentDepth-1)[1]
            if value > best_move:
                best_move = value
                best_board = minBoard

    else:
        raise Exception("bestMove is set to something other than inf or -inf")
    return(best_board, best_move)

def staticEval(evalBoard):
    """
        Evaluates a board for how advantageous it is
        -INF if WHITE wins
        INF if RED wins
        Otherwise use a particular strategy to evaluate the move
    """
    if evalBoard.gameWon == evalBoard.RED:
        return float('inf')
    elif evalBoard.gameWon == evalBoard.WHITE:
        return float('-inf')

    score = 0
    pieces = None
    if evalBoard.turn == evalBoard.WHITE:
        pieces = evalBoard.whitelist
        scoremod = -1
    elif evalBoard.turn == evalBoard.RED:
        pieces = evalBoard.redlist
        scoremod = 1

    distance = 0
    for piece1 in pieces:
        for piece2 in pieces:
            if piece1 == piece2:
                continue
            dx = abs(piece1[0] - piece2[0])
            dy = abs(piece1[1] - piece2[1])
            distance += dx ** 2 + dy ** 2
        distance /= len(pieces)
        score = 1.0 / distance * scoremod

        return score