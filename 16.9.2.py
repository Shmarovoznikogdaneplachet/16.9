class Rectangle:
    def __init__(self, width, heigh):
        self.width = width
        self.heigh = heigh
    def get_info(self):
        return self.width * self.heigh
rect_1 = Rectangle(5, 10)
print('Площадь =', rect_1.get_info())