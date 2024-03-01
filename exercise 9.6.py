from cs1graphics import*

class Star(Polygon):
    def __init__(self,numRays=5,outerRadius=10,innerRatio=5,center=Point(0,0)):
        Polygon.__init__(self)
        top=Point(0,-outerRadius)
        angle = 180.0 /numRays

        for i in range(numRays):
            self.addPoint(top ^ (angle*(2*i)))
            self.addPoint(innerRatio*top ^ (angle * (2*i+1)))

        self.adjustReference(0,outerRadius)  #dondurme referans noktamız, silinirse (0,0) alinir
        self.move(center.getX(),center.getY())
        self._innerRatio = innerRatio

    def setInnerRatio(self,newRatio):
        factor = newRatio / self._innerRatio
        self._innerRatio = newRatio
        for i in range(1,self.getNumberOfPoints(),2):
            self.setPoint(factor*self.getPoint(i),i)

    



star = Star(numRays=5, outerRadius=50, innerRatio=0.5, center=Point(100, 100))

# Döndürme referans noktası
star.adjustReference(0, -50)  # Yıldızın üst noktası

canvas = Canvas(300, 300)
star.setFillColor('blue')

canvas.add(star)

star.rotate(45)
