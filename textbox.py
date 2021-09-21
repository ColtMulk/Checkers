# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		Colton Mulkey
# 	 		Zachary Armstrong
# 	 		Aida Khalfaoui
# Section:		201
# Assignment:	lab -
# Date:		10/1/18
from graphics import *
class textbox():
    x = 0
    y = 0
    height = 0
    length = 0
    text = ""
    box = 0
    def __init__(self,x,y, width, length, text, size, color):
        """Initializizes text box object
        takes as input x and y of the center of the text box
        text is test to be printed
        width and length are the distance from the center point to the outlining rectangle"""
        self.x = x
        self.y = y
        self.height = width
        self.length = length
        self.text = Text(Point(x,y), text)
        self.text.setSize(size)
        self.text.setTextColor(color)
        self.box = Rectangle(Point(self.x - self.length, self.y - self.height),
                        Point(self.x + self.length, self.y + self.height))

    def isInside(self, x, y):
        """returns true if x and y our inside hit box"""
        if(x > self.x-self.length and x < self.x+self.length and y > self.y - self.height and y < self.y +self.length):
            return True
        return False

    def print(self,window):
        """draws textbox to screen"""
        self.text.draw(window)
        if(not (self.box.getP1() == self.box.getP2())):
            self.box.draw(window)

    def changeText(self,text):
        """changes text of textbox and undraws the box and text"""
        self.text.setText(text)
        self.text.undraw()
        self.box.undraw()