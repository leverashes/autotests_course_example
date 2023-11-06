# isinstance / issubclass

class Goods:

    def __init__(self, name, weight, price):
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name} Вес {self.weight} Цена {self.price}')


class Laptop(Goods):
    # + 1 характеристика OS_VERSION
    def __init__(self, name, weight, price, os_version):
        super().__init__(name, weight, price)
        self.os_version = os_version


class TV(Goods):
    pass


asus_laptop = Laptop('Asus', 1, 30000, 'windows10')
print('asus_laptop это телевизор', isinstance(asus_laptop, TV))
print('asus_laptop это ноутбук?', isinstance(asus_laptop, Laptop))
print("asus_laptop это товар?", isinstance(asus_laptop, Goods))
print("asus_laptop это ноутбук или телевизор?", isinstance(asus_laptop, (Laptop, TV)))