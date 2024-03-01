class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def printInfo(self):
        print('Name:',self.name)
        print('Age:',self.age)

# class Student:
#     def __init__(self,name,age,id) :
#         self.name = name
#         self.age = age
#         self.id = id

#     def printInfo(self):
#         print('Name:',self.name)
#         print('Age:',self.age)
#         print('ID:',self.id)
        
class Student(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)  ## Person sinifindaki self.name ve self.age kodları
        self.id=id

    def printInfo(self):
        super().printInfo()  #Person sınıfındaki name ve age yazdırma kodları
        print('ID:',self.id)

a=Person('Ahmet',18)
b=Student('Ayse',20,730)

print(a.name,a.age)
print(b.name,b.age,b.id)

