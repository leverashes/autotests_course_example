# protected / private
class Employee:

    def __init__(self, name, position):
        self.__name = name
        self.position = position

    def get_name(self):
        return self.__name.upper()

    def set_name(self, name):
        assert type(name) == str
        self.__name = name


ivan = Employee('Иванов иван', 'тестИровщиК')
print(ivan.get_name())
