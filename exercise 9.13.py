from cs1graphics import*
class LabeledRectangle(Layer):
    def __init__(self, message, width, height):
        Layer.__init__(self)
        
        self._message = TextBox(width,height)
        self._message.setMessage(message)
        
        
    def setFillColor(self, color):
        self._message.setFillColor(color)

    def _draw(self):
        self._beginDraw()
        Layer._draw(self)          
        self._message._draw()
        self._completeDraw()

if __name__ == '__main__':
  paper = Canvas()
  sign = LabeledRectangle('Rent a Car', 180, 50)
  sign.move(100,100)
  sign.setFillColor('gray')
  paper.add(sign)
