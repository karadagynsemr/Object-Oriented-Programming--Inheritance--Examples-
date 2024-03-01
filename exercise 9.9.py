from cs1graphics import*

class Square(Rectangle):
   def __init__(self, size=10, center=None):
    Rectangle.__init__(self, size, size, center) 

def setWidth(self, width):
    self.setSize(width)

def setHeight(self, height):
    self.setSize(height)

def setSize(self, size): 
    Rectangle.setWidth(self, size) 
    Rectangle.setHeight(self, size)

def getSize(self): 
   return self.getWidth( )

# parent version of this method # parent version of this method

class FlawedSquare(Square):
    def setWidth(self, size):
        self.setSize(size)

    def setHeight(self, size):
        self.setSize(size)

        
