class Myclass:
    def __init__(self):
        self._x = 1

    def increase(self):
        self._x +=1
    
class MyOtherClass(Myclass): #inheritance icin sadece sinif ismi kullanilir
    def __init__(self,z):    
        Myclass.__init__(self) #self gerekli
        self._x =z

    def decrease(self):
        self._x -=1 #self gerekli

a = Myclass()
b = MyOtherClass(3) # z degeri gerekli
b.increase()
# a.decrease() # Attribute error ----decrease fonksiyonu MyClass sinifina ait degil

print(a._x)
print(b._x)

        



