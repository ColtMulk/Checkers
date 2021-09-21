from graphics import *
from math import *
import validmove
from simpleAI import *
from textbox import *
from mainMenu import *
import complexAI

class cell:
    """one cell which contains the color of the cell and whether it has a piece on it and its attributes"""
    piece = ""
    cellC = ""
    king = False
    length = 10
    x = 0
    y = 0
    def __init__(self, color, cell, xcord, ycord, length):
        """initialize color of piece
         '' if there isn't one"""
        self.piece = color
        self.cellC = cell
        self.x = xcord
        self.y = ycord
        self.length = length

    def print(self, window):
        """prints cell to screen
        takes in a window to draw to"""

        x = self.x
        length = self.length
        y = self.y
        pt = Point(x,y)
        rect = Rectangle(pt, Point(x+length, y -length))
        rect.setFill(self.cellC)
        rect.draw(window)
        #checks if theres a piece and prints if there is
        if(self.piece != ""):
            circle = Circle(Point(x+length/2, y -length/2), (length/2)-1)
            circle.setFill(self.piece)
            circle.draw(window)
            if(self.king == True):
                #prints King label if its a king
                text = Text(circle.getCenter(),"K")
                text.draw(window)





#initializes board
def setup(length, xspace, yspace):
    """This creates a board setup for the beginning of a checkers game
    length is the size of the squares
    xspace is the space between the left side of the window and the start of the board
    yspace is the space between the top side of the window and the board"""
    w, h = 8,8
    board = [[0 for x in range(w)] for y in range(h)]
    length = length
    for row in range(0,8):
        for col in range(0,8):
            #white pieces
            if ((row+col)%2 == 1) and (row < 3):
                x = cell('white', 'green', col*length+xspace,row*length+length+yspace, length)
                board[row][col] = x
            #red pieces
            elif ((row+col)%2 == 1) and (row > 4):
                x = cell('red', 'green', col * length+xspace, row * length+length+yspace, length)
                board[row][col] = x
            #empty black square
            elif (row+col)% 2 == 0:
                x = cell("", 'black', col*length+xspace,row*length+length+yspace,length)
                board[row][col] = x
            #empty green squares
            else:
                x = cell("","green", col*length+xspace,row*length+length+yspace, length)
                board[row][col] = x
    return board


class game():
    """creates a new game of checkers"""
    board = 0
    piecesW = 0
    piecesR = 0
    window = 0
    length = 50
    xyspace = 180
    yspace = 100
    def __init__(self, length, squareSize):
        """takes in squaresize and length
        setup window, number of pieces and board for game"""
        self.window = GraphWin("board", length*1.2,length)
        self.board = setup(squareSize, self.xyspace, self.yspace)
        self.length = squareSize
        self.piecesR = 12
        self.piecesW = 12

    def printBoard(self):
        """prints the board to game window"""
        #printss the board and checker pieces
        board = self.board
        for row in board:
            for cell in row:
                cell.print(self.window)
        size = self.window.getWidth()
        pt = Point(size / 2, 50)
        #prints title
        title = Text(pt, "Checkers")
        title.setSize(30)
        title.setTextColor("black")
        title.draw(self.window)
        self.window.setBackground("gray")
        cir = Circle(Point(size / 4, 50), 10)
        cir.setFill("white")
        redcir = Circle(Point(size / 4 * 3, 50), 10)
        redcir.setFill("red")
        cir.draw(self.window)
        redcir.draw(self.window)
    def movePiece(self, row,col,row2,col2, window):
        """moves piece at row col to row2 col2
        row and col are indexs for board
        takes in window to print to"""
        self.board[row2][col2].piece = self.board[row][col].piece
        self.board[row][col].piece = ""
        if(self.board[row][col].king):
            self.board[row2][col2].king = True
            self.board[row][col].king = False
        self.board[row2][col2].print(window)
        self.board[row][col].print(window)

    def changeColor(self, row, col, color, window):
        """changes color of row col to color and returns previous color"""
        prev = self.board[row][col].cellC
        self.board[row][col].cellC = color
        self.board[row][col].print(window)
        return prev

    def checkKing(self, row, col):
        """checks if piece has become a king and changes to one if it has"""
        if(row == 0 or row == 7):
            self.board[row][col].king = True


    def takePiece(self, row, col, row2, col2, window):
        """removes piece if move is jump"""
        if(abs(col2-col) == 2):
            nrow = max(row,row2) -1
            ncol = max(col,col2)-1
            self.board[nrow][ncol].piece = ""
            self.board[nrow][ncol].print(window)
            return True
        return False




    def startGame(self):
        """start game for 2player"""
        #input screen
        window = self.window
        piecesW = self.piecesW
        piecesR = self.piecesR
        turn = 'white'
        #draw board and Exit button
        self.printBoard()
        exit = textbox(window.getWidth() - 50, 20, 20, 50, "Exit", 20, "black")
        exit.print(window)
        #creates display for red and white pieces
        wtext = "White Pieces: " + str(piecesW)
        rtext = "Red Pieces: " + str(piecesR)

        white = textbox(window.getWidth()/4, window.getHeight()-100, 0, 0, wtext, 20, "black")
        red = textbox(window.getWidth()/4*3, window.getHeight()-100, 0 ,0, rtext, 20, "black")
        red.print(window)
        white.print(window)
        #creates display for whose turn it is
        turnW = "Turn: White"
        turnR = "Turn: Red"
        turnT = textbox(window.getWidth()/2,window.getHeight()-50, 0, 0, turnW, 20, "black")
        turnT.print(window)
        #creates draw button
        drawT = "Draw"
        draw = textbox(window.getWidth()-50,100,20,50, drawT, 20, "black")
        draw.print(window)
        while(piecesW != 0 and piecesR != 0):
            # prints whose turn it is
            if(turn=='white'):
                turnT.changeText(turnW)
            else:
                turnT.changeText(turnR)
            turnT.print(window)
            #gets user input
            pt = self.window.getMouse()
            #checks if click is in exit rectangle
            if(exit.isInside(pt.x,pt.y)):
                exit()
            #checks if click in draw rectangle
            if(draw.isInside(pt.x,pt.y)):
                print("Draw")
                exit()
            col = floor((pt.x-self.xyspace) / self.length)
            row = floor((pt.y-self.yspace) / self.length)
            #checks whose turn it is
            print(turn)
            if(turn == 'white'):
                try:
                    #highlights selected square
                    prevC = self.changeColor(row,col,'red', window)
                    #gets second user input
                    pt2 = self.window.getMouse()
                    col2 = floor((pt2.x-self.xyspace) / self.length)
                    row2 = floor((pt2.y-self.yspace) / self.length)

                    #chagnes color back
                    self.changeColor(row,col, prevC, window)
                    #checks if piece selected is a king
                    if (self.board[row][col].king):
                        #checks if its a valid move for a king
                        if(validmove.checkKingValidity(self.board,row,col,row2,col2, turn)):
                            #checks if piece was taken
                            if(self.takePiece(row, col, row2, col2,window)):
                                piecesR-=1
                                #changes text for number of red pieces
                                rtext = "Red pieces: " + str(piecesR)
                                red.changeText(rtext)
                                red.print(window)
                            self.movePiece(row, col,row2,col2, window)
                            turn = 'red'
                    #checks if white move is valid
                    elif(validmove.checkwhitevalidity(self.board, row, col, row2, col2)):
                        #checks if piece was taken
                        if(self.takePiece(row, col, row2, col2, self.window)):
                            piecesR-=1
                            #updates number of red pieces
                            rtext = "Red pieces: " + str(piecesR)
                            red.changeText(rtext)
                            red.print(window)
                        #checks if piece is king and moves piece
                        self.checkKing(row2,col2)
                        self.movePiece(row,col,row2,col2, window)
                        #changes turn
                        turn = 'red'
                    else:
                        print("Invalid input")

                except:
                    print("Error")
            else:
                try:
                    #highlights selected square
                    prevC = self.changeColor(row, col, 'red', window)
                    #gets second user input
                    pt2 = self.window.getMouse()
                    col2 = floor((pt2.x-self.xyspace) / self.length)
                    row2 = floor((pt2.y-self.yspace) / self.length)
                    self.changeColor(row,col, prevC, window)
                    # check if valid movement
                    #checks if its a king
                    if (self.board[row][col].king):
                        #checks if its a valid move for a king
                        if(validmove.checkKingValidity(self.board,row,col,row2,col2, turn)):
                            #checks if piece was taken
                            if(self.takePiece(row, col, row2, col2,window)):
                                piecesW-=1
                                #changes text for number of white pieces
                                wtext = "White pieces: " + str(piecesW)
                                white.changeText(wtext)
                                white.print(window)
                            self.movePiece(row, col,row2,col2, window)
                            turn = 'white'
                    #checks if white move is valid
                    elif(validmove.checkredvalidity(self.board, row, col, row2, col2)):
                        #checks if piece was taken
                        if(self.takePiece(row, col, row2, col2, self.window)):
                            piecesW -= 1
                            # changes text for number of white pieces
                            wtext = "White pieces: " + str(piecesW)
                            white.changeText(wtext)
                            white.print(window)
                        #checks if piece is king and moves piece
                        self.checkKing(row2,col2)
                        self.movePiece(row,col,row2,col2, window)
                        #changes turn
                        turn = 'white'
                    else:
                        print("Invalid input")
                except:
                    pass
        #finds out who wins
        if (piecesR == 0):
            print("White Wins")
        elif (piecesW == 0):
            print("Red Wins")
        window.close()

    def startGameAi(self, difficulty):
        """start game for 2player"""
        # input screen
        window = self.window
        piecesW = self.piecesW
        piecesR = self.piecesR
        turn = 'white'
        # draw board and Exit button
        self.printBoard()
        exitb = textbox(window.getWidth()-50, 20, 20, 30, "Exit", 20, "black")
        exitb.print(window)
        #creates text for number of white and red pieces
        wtext = "White Pieces: " + str(piecesW)
        rtext = "Red Pieces: " + str(piecesR)

        white = textbox(window.getWidth() / 4, window.getHeight() - 100, 0, 0, wtext, 20, "black")
        red = textbox(window.getWidth() / 4 * 3, window.getHeight() - 100, 0, 0, rtext, 20, "black")
        red.print(window)
        white.print(window)
        while (piecesW != 0 and piecesR != 0):

            # checks if click is in exit rectangle



            # checks whose turn it is
            if (turn == 'white'):
                try:
                    #user input
                    pt = self.window.getMouse()
                    col = floor((pt.x - self.xyspace) / self.length)
                    row = floor((pt.y - self.yspace) / self.length)
                    if (exitb.isInside(pt.x, pt.y)):
                        break
                    #highlights selection
                    prevC = self.changeColor(row, col, 'red', window)
                    #second user input
                    pt2 = self.window.getMouse()
                    col2 = floor((pt2.x - self.xyspace) / self.length)
                    row2 = floor((pt2.y - self.yspace) / self.length)

                    self.changeColor(row, col, prevC, window)
                    #checks if valid move
                    if (self.board[row][col].king):
                        if(validmove.checkKingValidity(self.board,row,col,row2,col2,turn)):
                            if (self.takePiece(row, col, row2, col2, window)):
                                #updates pieces
                                piecesR -= 1
                                rtext = "Red pieces: " + str(piecesR)
                                red.changeText(rtext)
                                red.print(window)
                        #moves piece and changes turn
                        self.movePiece(row, col, row2, col2, window)
                        turn = 'r'
                    elif (checkwhitevalidity(self.board, row, col, row2, col2)):
                        if (self.takePiece(row, col, row2, col2, self.window)):
                            #updates pieces
                            piecesR -= 1
                            rtext = "Red pieces: " + str(piecesR)
                            red.changeText(rtext)
                            red.print(window)
                        #checks if king, moves piece and switches turn

                        self.checkKing(row2, col2)
                        self.movePiece(row, col, row2, col2, window)
                        turn = 'R'
                    else:
                        print("Invalid input")

                except:
                    print("invalid selection!")
            else:
                #gets AI's move
                row, col, row2,col2 = findRedMoves(self.board)
                self.checkKing(row2,col2)
                self.movePiece(row, col, row2, col2, window) #moves piece

                turn = "white"
                if (self.takePiece(row, col, row2, col2, window)): #takes piece
                    #updates pieces
                    piecesW -= 1
                    wtext = "White pieces: " + str(piecesW)
                    white.changeText(wtext)
                    white.print(window)
        #decides who won and closes game
        if(piecesR == 0):
            print("White Wins")
        elif(piecesW==0):
            print("Red Wins")

        window.close()





#opens main menu
main = mainMenu(500)
main.draw()
while(True):
    pt = main.getClick()
    x=0
    if(main.isComp(pt.x,pt.y)):
        x = 1
        break
    elif(main.isTwoPlayer(pt.x,pt.y)):
        x = 2
        break

main.closeMenu()
try:
    if(x == 1):
        #difficulty = input("Enter difficulty: ")
        game = game(700, 60)
        game.startGameAi(4)
    else:
        game = game(700, 60)
        game.startGame()
except:
    print("error")




