# str / rep
class Cats:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Порода: {self.breed}\n'
            f'Возраст: {self.age}\n'
        )

    def __repr__(self):
        return f'Имя: {self.name}'


murzic = Cats('Мурзик', 'Сфинкс', 1)
print(murzic)