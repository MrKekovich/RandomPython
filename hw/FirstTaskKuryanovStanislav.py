class HomeWork:
    name = ''
    surname = ''
    age = 0

    def __init__(self):
        self.name = input('Enter name: ')
        self.surname = input('Enter surname: ')
        self.age = int(input('Enter age: '))

        print(f'Меня зовут {self.name} {self.surname}. Мой возвраст - {self.age}')


user = HomeWork()
