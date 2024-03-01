from cs1graphics import*

class Mailbox(Layer):

    def __init__(self,flagUp=False,doorOpen=False,color='yellow'): 
        super().__init__()

        self._post = Rectangle(16,80,Point(0,-40))
        self._post.setFillColor('black')
        self._box = Rectangle(50,30,Point(0,-90))
        self._box.setFillColor(color)
        self._door = Rectangle(6,30,Point(25,-90))
        self._door.setFillColor(color)
        self._door.adjustReference(-3,15)
        self._doorOpen = doorOpen
        if doorOpen:
            self._door.rotate(90)

        self._flag = Polygon(Point(15, -100), Point(15, -106), Point(-15, -106),
        Point(-15, -90), Point(-5, -90), Point(-5, -100))
        self._flag.setFillColor('red')
        self._flag.adjustReference(-3,-3)
        self._flagUp = flagUp
        if flagUp:
            self._flag.rotate(90)


        self.add(self._post)
        self.add(self._box)
        self.add(self._door)
        self.add(self._flag)

    def setColor(self,color):
        self._box.setFillColor(color)
        self._door.setFillColor(color)

    def doorIsOpen(self):
        return self._doorOpen
    
    def openDoor(self):
        if not self._doorOpen:
            for i in range(90):
                self._door.rotate(1)
            self._doorOpen = True

    def closeDoor(self):
        if self._doorOpen:
            for i in range(90):
                self._door.rotate(-1)
            self._doorOpen = False

    def flagIsUp(self):
        return self._flagUp
    
    def toogleFlag(self):
        if self._flagUp:
            increment = -1
        else:
            increment=1
        for i in range(90):
            self._flag.rotate(increment)
        self._flagUp = not self._flagUp

    
if __name__ == "__main__":
    paper = Canvas(400,400)
    box = Mailbox()
    box.move(150,200)
    paper.add(box)
    input('Press Return to Continue')

    box.toogleFlag()
    input('Press Return to Continue')

    box.setColor('orange')
    input('Press Return to Continue')

    box.toogleFlag()
    box.openDoor()
    input('Press Return to Continue')

    box.scale(1.25)
    input('Press Return to Continue')

    box.closeDoor()
    input('Press Return to End')









    
