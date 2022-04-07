class Wallet:
    def __init__(self, name, surname, cash):
        self.name = name
        self.surname = surname
        self.cash = cash
    def get_info(self):
        return f'({self.name}, {self.surname}, {self.cash})'
money_1 = Wallet('Иван', "Петров", 50)
print(money_1.get_info())
