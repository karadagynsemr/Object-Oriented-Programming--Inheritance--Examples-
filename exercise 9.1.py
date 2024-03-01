class Sneetch:
    def __init__(self):
        self._a = 3
        self._b = 4

    def x(self):
        print(self._a)

    def y(self):
        print(self._b)

class StarBellySneetch(Sneetch):
        
    def __init__(self):
        Sneetch.__init__(self)
        self._b = 7
        self._c = 8

    def y(self):
        print(self._b,self._c)

    def z(self):
        print(self._a,self._c)

alice = Sneetch()
bob = StarBellySneetch()

alice.x() #a değerini yazar  3.
alice.y() #b değerini yazar  4.
#alice.z() #AttributeError hatası verir çünkü Sneetch sınıfında z adında bir metot yok.
bob.x() #a değerini yazar 3. x metodu Sneetch'den alınır
bob.y() #b ve c değerlerini yazar  7 ve 8. StarBellySneetch sınıfındaki y metodu yeniden tanımladnığı için Sneetch sınıfındaki y metodunu geçersiz kılar.
bob.z() #a ve c değerlerini yazar  3 ve 8. 
