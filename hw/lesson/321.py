class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self._name}: Гав")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self._name}: Мяу")


class Nursery:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def noise(self):
        for animal in self.animals:
            animal.speak()


print('Питомник Солнышко:')
nursery1 = Nursery('Солнышко')

nursery1.add_animal(Dog('Барсик', 2))
nursery1.add_animal(Cat('Мурзик', 1))
nursery1.add_animal(Dog('Шарик', 1))
nursery1.add_animal(Dog('Шарик', 1))
nursery1.noise()

print('Питомник Облачко:')
nursery2 = Nursery('Облачко')

dog = Dog('Барсик', 2)
dog._name = 'Прекол'

nursery2.add_animal(dog)
nursery2.noise()


