class Area:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width

class Square(Area):
    def __init__(self, side):
        super().__init__(side, side)

a = Area(2,3)
print(a.area())

s = Square(2)
print(s.area())