# аттрибуты класса != аттрибуты экземляра класса
class Cats:

    MAX_AGE = 36

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        if age > self.MAX_AGE:
            self.__class__.MAX_AGE = age



print(Cats.MAX_AGE)
murzic = Cats('murzic', 'russian', 37)
barsik = Cats('barsik', 'russian', 3)
print(murzic.MAX_AGE)
print(barsik.MAX_AGE)

# print(murzic.MAX_AGE)
# print(barsik.MAX_AGE)

print(murzic.__dict__)
print(murzic.__class__.__dict__)