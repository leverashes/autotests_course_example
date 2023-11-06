# property
class Employee:

    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    @property
    def name(self):
        return self.__name.upper()

    @name.setter
    def name(self, value):
        assert type(value) == str
        self.__name = value


ivan = Employee('Иванов иван', 'тестИровщиК')
ivan.name = 'Дмитрием дмитрий'
print(ivan.name)
