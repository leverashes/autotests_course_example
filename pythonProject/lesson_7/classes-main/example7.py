# наследование

class Goods:

    def __init__(self, name, weight, price):
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def set_name(self, name):
        self.name = name

    def print_info(self):
        print(f'{self.name} Вес {self.weight} Цена {self.price}')


class Laptop(Goods):
    # + 1 характеристика OS_VERSION
    def __init__(self, name, weight, price, os_version):
        super().__init__(name, weight, price)
        self.os_version = os_version

    def print_info(self):
        print(f'{self.name} Вес {self.weight} Цена {self.price} OC: {self.os_version}')


asus = Laptop('Asus', 1, 30000, 'windows10')
asus.set_name('Asus prime')
