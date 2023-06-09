# В этот раз отдохнём от всех заморочек.
import time


class Utils:
    @staticmethod
    def get_valid_input(prompt, data_type):
        while True:
            user_input = input(prompt)
            try:
                value = data_type(user_input)
                return value
            except ValueError:
                print(f'Ошибка: "{user_input}" невозможно преобразовать в {data_type.__name__}.')


class Recommend:
    def __init__(self, taste):
        try:
            self.taste = taste.lower()
        except Exception as e:
            exit(e)

    def recommend(self):
        if self.taste == 'ванильный':
            return 'Рекомендуем вам чизкейк'
        elif self.taste == 'ореховый':
            return 'Рекомендуем вам ореховый торт'
        else:
            return 'Такого у нас в меню нет'


class CalculatePrice:
    def __init__(self, price=0):
        self.price = price

    def get_prices(self):
        while True:
            user_input = Utils.get_valid_input('Введите цену (0 для выхода): ', float)
            if user_input == 0:
                return f'стоимость без скидки: {self.price} \n стоимость со скидкой: {self.calculate}'
            elif user_input < 0:
                print('Ошибка: должно быть положительное число')
            else:
                self.price += user_input

    @property
    def calculate(self):
        return self.price * 0.9


logo = """
  __  __          _  __         _                      _          _     
 |  \/  |        | |/ /        | |                    (_)        | |    
 | \  / |  _ __  | ' /    ___  | | __   ___   __   __  _    ___  | |__  
 | |\/| | | '__| |  <    / _ \ | |/ /  / _ \  \ \ / / | |  / __| | '_ \ 
 | |  | | | |    | . \  |  __/ |   <  | (_) |  \ V /  | | | (__  | | | |
 |_|  |_| |_|    |_|\_\  \___| |_|\_\  \___/    \_/   |_|  \___| |_| |_|""".replace('\n', '\n;').split(';')


def delay(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass


def animate_logo():
    for i in logo:
        for j in i:
            print(j, end='')
            if j != ' ':
                delay(0.001)


def main():
    animate_logo()
    while True:
        print("""
        1. Выбор вкуса
        2. Расчёт цены
        0. Выход""")
        task = input('Выберите задание: ')
        if task == '1':
            taste = input('Введите вкус: ')
            recommend = Recommend(taste)
            print(recommend.recommend())
        elif task == '2':
            price = CalculatePrice()
            print(price.get_prices())
        elif task == '0':
            break


if __name__ == '__main__':
    main()
