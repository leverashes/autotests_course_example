# класс

class Cats:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = 0

    def print_data(self):
        print(
            f'Имя: {self.name}\n'
            f'Порода: {self.breed}\n'
            f'Возраст:{self.age}\n'
            f'Вес: {self.weight}\n'
        )

    def set_weight(self, weight):
        self.weight = weight
        self.print_data()


murzic = Cats('Мурзик', 'Сфинкс', 1)
murzic.set_weight(1)
sema = Cats('Сема', 'Мейн-кун', 5)


cats_list = [
    murzic,
    sema,
    Cats('Барсик', 'Британец', 3),
]

for cat in cats_list:
    cat.print_data()
