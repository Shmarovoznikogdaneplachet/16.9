class Rectangle:
    def __init__(self, x, y, width, heigh):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = heigh
    def get_area(self):
        return f'(Координата x = {self.x}, Координата y = {self.y}, Ширина прямоугльника = {self.width}, Высота прямоугольника  = {self.heigh})'
amount_Rectangle = Rectangle (5, 10, 50, 100)
print(amount_Rectangle.get_area())