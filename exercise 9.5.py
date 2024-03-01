class SortedSet:

    def __init__(self,initial=None):
        self._items=list()
        if initial:
            self.extend(initial)


    # def indexAfter(self,value):
    #     walk=0
    #     while walk < len(self._items) and value >= self._items[walk]:
    #        walk+=1
    #     return walk
            
    def indexAfter(self,value):
        walk=0
        while walk < len(self) and value >= self[walk]:   #indexlemeyi yanlis yapar 
            walk+=1
        return walk

    def insert(self,value):
        if value not in self._items:
            place = self.indexAfter(value)
            self._items.insert(place,value)

    def extend(self,other):
        for element in other:
            self.insert(element)

    def __add__(self,other):
        result = SortedSet(self)
        result.extend(other)
        return result

    def index(self,value):
        return self._items.index(value)

    def remove(self,element):
        self._items.remove(element)

    def pop(self,index=None):
        return self._items.pop(index)

    def __contains__(self,element):
        return element in self._items

    def __getitem__(self,index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __eq__(self,other):
        return self._items == other.items

    def __it__(self,other):
        return self._items < other.items

    def __str__(self):
        return str(self._items)


s1 = SortedSet([5, 2, 3, 1, 4])

# print("s1: ", s1._items)

# #  eleman ekle
# s1.insert(6)
# print("s1 after insert: ", s1._items)

# # Bir elemanı silin
# s1.remove(2)
# print("s1 after remove: ", s1._items)

# #  index bulma
# index = s1.index(3)
# print("Index of 3: ", index)

# # elemen kontrol
# contains = 4 in s1
# print("Is 4 in s1? ", contains)

# # indexten eleman cagir
# element = s1[2]
# print("Element at index 2 : ", element)

# # Listenin uzunluğu
# length = len(s1)
# print("Length of s1: ", length)

# # Başka bir SortedSet 
# s2 = SortedSet([7, 8, 9,5,3])

print(type(s1))
print(type(s1._items))

