
from cs1graphics import *

class LabeledRectangle(Layer):
    def __init__(self, message, width, height):
        Layer.__init__(self)
        self._text = Text(message)
        self._message = TextBox(width,height)
        self._message.setMessage(message)

    def _draw(self):
        self._beginDraw()
        Layer._draw(self)          # access the overridden Rectangle version of _draw
        self._message._draw()
        self._completeDraw()

    def setFillColor(self, color):
        self._message.setFillColor(color)
    
    def signaturecrop(self,padding=5):
        dims = self._text.getDimensions()
        self._message.setWidth(dims[0]+padding)
        self._message.setHeight(dims[1]+padding) 

if __name__ == '__main__':
    paper = Canvas(300,300)
    sign = LabeledRectangle('Real Estate', 200, 100)
    sign.move(100,100)
    sign.setFillColor('gold')
    sign.signaturecrop(20)
    paper.add(sign)
