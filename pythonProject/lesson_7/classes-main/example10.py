# множественное наследование
class Goods(object):

    def __init__(self, name, weight, price):
        print('init Goods')
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name} Вес {self.weight} Цена {self.price}')


class LoggingSale:

    ID = 0

    def __init__(self):
        print('init Mixin')
        self.__class__.ID += 1
        self.id = self.ID

    def save_sale_log(self):
        print(f'Продали товар №{self.id}')


class Laptop(Goods, LoggingSale):

    def __init__(self, name, weight, price, os_version):
        super().__init__(name, weight, price)
        self.os_version = os_version


l = Laptop('Asus', 1, 50000, 'linux')
l.print_info()
print(Laptop.mro())
l.save_sale_log()
# print(Laptop.mro())
# acer = Laptop('Acer', 2, 30000)
# acer.save_sale_log()