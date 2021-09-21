from graphics import *
from textbox import *
class mainMenu:
    """main menu of game"""
    window = 0
    title = 0
    computer = 0
    size = 0
    twoPlayer = 0
    exitb = 0

    def __init__(self, size):
        """initializes main menu"""
        self.window = GraphWin("Menu", size, size)
        self.size = size
        pt = Point(size/2, 50)
        self.title = Text(pt, "Checkers")
        self.title.setSize(30)
        self.title.setTextColor("black")
        self.computer = textbox(size/4,size/2,size/10,size/5,"Comp", 20, "black")
        self.twoPlayer = textbox(size/4*3, size/2, size/10,size/5, "Two Player", 20, "black")
        self.exitb = textbox(self.window.getWidth() - 50, self.window.getHeight()-30, 20, 30, "Exit", 20, "black")


    def draw(self):
        """draws main menu"""
        self.window.setBackground("green")
        cir = Circle(Point(self.size/4, 50), 10)
        cir.setFill("white")
        redcir = Circle(Point(self.size/4*3, 50), 10)
        cir.draw(self.window)
        redcir.draw(self.window)
        redcir.setFill("red")
        self.exitb.print(self.window)

        self.title.draw(self.window)
        self.computer.print(self.window)
        self.twoPlayer.print(self.window)

    def isComp(self, x, y):
        """checks if given point is in AI slot"""
        if(self.computer.isInside(x,y)):
            return True
        return False

    def isTwoPlayer(self, x, y):
        """checks if given point is in a two Player box"""
        if(self.twoPlayer.isInside(x,y)):
            return True
        return False

    def closeMenu(self):
        """Closes window"""
        self.window.close()

    def getClick(self):
        """gets mouse click and returns point"""
        pt = self.window.getMouse()
        if(self.exitb.isInside(pt.x,pt.y)):
            exit()
        return pt

