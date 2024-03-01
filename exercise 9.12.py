from cs1graphics import *

class Mailbox(Drawable):
    def __init__(self, flagUp=False, doorOpen=False, color='white'):
        Drawable.__init__(self)                      

        self._post = Rectangle(16, 80, Point(0,-40))
        self._post.setFillColor('brown')

        self._box = Rectangle(50, 30, Point(-3,-95))
        self._box.setFillColor(color)

        self._door = Rectangle(6, 30, Point(25,-95))
        self._door.setFillColor(color)
        self._door.adjustReference(-3, 15)            
        self._doorOpen = doorOpen

        if doorOpen:
            self._door.rotate(90)
        self._flag = Polygon(Point(15,-100), Point(15,-106), Point(-15,-106),
                            Point(-15,-90), Point(-5,-90), Point(-5,-100))
        self._flag.setFillColor('red')
        self._flag.adjustReference(-3,-3)             # act as rivot holding flag
        self._flagUp = flagUp

        if flagUp:
            self._flag.rotate(90)

        self.envelope = Envelope()

    

    def _draw(self):
        self._beginDraw()                             # required protocol
        self._post._draw()
        self._box._draw()
        self._door._draw()
        self._flag._draw()
        self._completeDraw()                          # required protocol

    def setColor(self, color):
        self._box.setFillColor(color)
        self._door.setFillColor(color)

    def doorIsOpen(self):
        return self._doorOpen
  
    def openDoor(self):
        if not self._doorOpen:
            for i in range(90):                         # animate the motion
                self._door.rotate(1)
        self._doorOpen = True

    def closeDoor(self):
        if self._doorOpen:
            for i in range(90):                         # animate the motion
                self._door.rotate(-1)
        self._doorOpen = False

    def flagIsUp(self):
        return self._flagUp
  
    def toggleFlag(self):
        if self._flagUp:
            increment = -1
        else:
            increment = 1
        for i in range(90):                           # animate the motion
            self._flag.rotate(increment)
        self._flagUp = not self._flagUp

class Envelope(Drawable):
    def __init__(self, color='white'):
        Drawable.__init__(self)
        self._color = color
        self._width = 25
        self._height = 14
        self._body = Rectangle(self._width, self._height, Point(0,0))
        self._triangle = Polygon(Point(-self._width/2,0), Point(0,self._height/2), Point(self._width/2,0))
        self._body.setFillColor(self._color)
        self._triangle.setFillColor("red")
        self._triangle.move(0, -self._height/2)

    def _draw(self):
        self._beginDraw()
        self._body._draw()
        self._triangle._draw()
        self._completeDraw()



if __name__ == "__main__":
  x = 150
  y = 200
  paper = Canvas(300,300)
  box = Mailbox()
  box.move(x,y)
  paper.add(box)
  input('Press Return to Continue')

  box.toggleFlag()
  input('Press Return to Continue')

  box.setColor('grey')
  input('Press Return to Continue')

  box.toggleFlag()
  box.openDoor()
  box.envelope.moveTo(x+50,y-100)
  paper.add(box.envelope)
  input('Press Return to Continue')

  box.scale(1.5)
  box.envelope.scale(1.5)
  box.envelope.moveTo((x+55),(y-100)/1.5)
  input('Press Return to Continue')

  box.closeDoor()
  paper.remove(box.envelope)
  input('Press Return to End')
  paper.close()
