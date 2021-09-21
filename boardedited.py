class cell():
    piece = ""
    cellC = ""
    length = 10
    x = 0
    y = 0
    RED = 1
    WHITE = 0
    NOTDONE = -1
    def __init__(self, color, cell, xcord, ycord):
        """initialize color of piece
         '' if there isn't one"""
        self.piece = color
        self.cellC = cell
        self.x = xcord
        self.y = ycord
        self.redlist = []
        self.whitelist = []
        for i in range(8):
            self.redlist.append((i, (i+1%2)))
            self.whitelist.append((i, 8 - (i%2) - 1))
        self.gameWon = self.NOTDONE
        self.boardState = [[' '] * 8 for x in range(8)]

    def print(self):
        if(self.piece != ""):
            pass


    def iterWhiteMoves(self):
        for piece in self.whitelist:
            for move in self.iterWhitePiece(piece):
                yield move

    def iterRedMoves(self):
        for piece in self.redlist:
            for move in self.iterRedPiece(piece):
                yield move

    def iterWhitePiece(self, piece):
        return self.iterBoth(piece, ((-1,-1),(1,-1)))

    def iterRedPiece(self, piece):
        return self.iterBoth(piece, ((-1,1),(1,1)))

    def iterBoth(self, piece, moves):
        for move in moves:
            targetx = piece[0] + move[0]
            targety = piece[1] + move[1]
            if targetx<0 or targetx >= 7 or targety < 0 or targety >= 7:
                continue
            target = (targetx, targety)
            red = target in self.redlist
            white = target in self.whitelist
            if not red and not white:
                yield (piece, target, self.NOTDONE)

            else:
                if board[piece[0]][piece[1]] == "Red" and red:
                    continue
                elif board[piece[0]][piece[1]] == "White" and white:
                    continue
                jumpx = target[0] + move[0]
                jumpy = target[1] + move[1]
                if jumpx < 0 or jumpx >= 8 or jumpy < 0 or jumpy >= 8:
                    continue
                jump = (jumpx, jumpy)
                red = jump in self.redlist
                white = jump in self.whitelist
                if not red and not white:
                    yield (piece, jump, self.turn)

    def updateBoard(self):
        for i in range(8):
            for j in range(8):
                self.boardState[i][j] = ""
        for piece in self.redlist:
            self.boardState[piece[1]][piece[1]] = "Red"
        for piece in self.whitelist:
            self.boardState[piece[1]][piece[1]] = "White"

    def moveSilentRed(self, moveFrom, moveTo, winLoss):
        if moveTo[0] < 0 or moveTo[0] >= 7 or moveTo[1] < 0 or moveTo >= 7:
            raise Exception("That would move red piece", moveFrom, "out of bounds")
        red = moveTo in self.redlist
        white = moveTo in self.whitelist
        if not (red or white):
            self.redlist[self.redlist.index(moveFrom)] = moveTo
            self.updateBoard()
            self.turn = self.WHITE
            self.gameWon = winLoss
        else:
            raise Exception

    def moveSilentWhite(self, moveFrom, moveTo, winLoss):
        if moveTo[0] < 0 or moveTo[0] >= self.width or moveTo[1] < 0 or moveTo[1] >= self.height:
            raise Exception("That would move white piece", moveFrom, "out of bounds")
        red = moveTo in self.redlist
        white = moveTo in self.whitelist
        if not (red or white):
            self.whitelist[self.whitelist.index(moveFrom)] = moveTo
            self.updateBoard()
            self.turn = self.RED
            self.gameWon = winLoss
        else:
            raise Exception

    def moveWhite(self, moveFrom, moveTo, winLoss):
        self.moveSilentWhite(moveFrom, moveTo, winLoss)

    def moveRed(self, moveFrom, moveTo, winLoss):
        self.moveSilentRed(moveFrom, moveTo, winLoss)

def setDifficulty(val):
    DIFFICULTY = val

DIFFICULTY = 2
w, h = 8,8
board = [[0 for x in range(w)] for y in range(h)]
length = 10
for row in range(0,8):
    for col in range(0,8):
        if ((row+col)%2 == 1) and (row < 4):
            x = cell('White', 'Green', col*length,row*length)
            board[row][col] = x
        elif ((row+col)%2 == 1) and (row > 5):
            x = cell('Red', 'Green', col * length, row * length)
            board[row][col] = x
        elif (row+col)% 2 == 0:
            x = cell("", 'Black', col*length,row*length)
            board[row][col] = x
        else:
            x = cell("","Green", col*length,row*length)
            board[row][col] = x

