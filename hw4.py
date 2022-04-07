class Volunteer:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

#Метод, возвращающий инфу о волонтере
    def get_info(self):
        return f'({self.name}, {self.surname}, {self.city})'
