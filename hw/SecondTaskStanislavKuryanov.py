# пользуемся библеотеками, чтобы отправить данные на сервер :P
import urllib.parse
import urllib.request
import time


class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height or width

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)


class FlightCost:
    def __init__(self, luggage_price, price_ticket):
        self.luggage_price = luggage_price
        self.price_ticket = price_ticket

    def total_cost(self):
        return self.luggage_price + self.price_ticket


class Reverse:
    def __init__(self, str_list):
        self.str_list = str_list[::-1]
        print(*self.str_list, sep='\n')

    def reverse(self):
        print(*self.str_list, sep='\n')


LOADING_BAR = """

  __  __          _  __         _                      _          _     
 |  \/  |        | |/ /        | |                    (_)        | |    
 | \  / |  _ __  | ' /    ___  | | __   ___   __   __  _    ___  | |__  
 | |\/| | | '__| |  <    / _ \ | |/ /  / _ \  \ \ / / | |  / __| | '_ \ 
 | |  | | | |    | . \  |  __/ |   <  | (_) |  \ V /  | | | (__  | | | |
 |_|  |_| |_|    |_|\_\  \___| |_|\_\  \___/    \_/   |_|  \___| |_| |_|
                                                                                                                       
"""


def loading_animation():
    for char in LOADING_BAR:
        if char == " ":
            print(char, end="", flush=True)
        else:
            print(char, end="", flush=True)
            time.sleep(0.001)


def task_manager(task_number):
    if task == '1':
        print('Задание 1:')
        strings = [input(f'Введите строку {i + 1}: ') for i in range(3)]
        reverse_string = Reverse(strings)
        return True
    elif task == '2':
        print('Задание 2:')
        review = input('Введите отзыв о данной программе: ')
        print(
            f'Ваш отзыв: {review}. Как и просили его длинна - {len(review)} символов с пробелом и {len(review.replace(" ", ""))} без пробелов'
        )
        accept_send_review = input('Хотите отправить отзыв? \n1. Да \n2. Нет \n Ваш выбор: ')
        if accept_send_review == '1':
            print(
                """Да, мне было просто скучно, поэтому я создал отдельный сайт на Laravel,
                 выложил его на vercel и сделал новую базу данных...
                 Посмотреть отзывы можно тут: https://review-accept-mrkekovich.vercel.app/"""
            )
        else:
            print('Отзыв не отправлен.')
        return True
    elif task == '3':
        print('Задание 3:')
        price_ticket = validate_input(input('Введите стоимость билета: '))
        luggage_price = validate_input(input('Введите стоимость багажа: '))
        flight_cost = FlightCost(luggage_price, price_ticket)
        print(f'Стоимость билета: {flight_cost.total_cost()}')
        return True
    elif task == '4':
        print('Задание 4:')
        side_a = validate_input(input('Введите сторону: '))
        square = Rectangle(side_a)
        print(f'Площадь квадрата: {square.area}')
        return True
    elif task == '5':
        print('Задание 5:')
        side_a = validate_input(input('Введите первую сторону: '))
        side_b = validate_input(input('Введите вторую сторону: '))
        rectangle = Rectangle(side_a, side_b)
        print(f'Площадь прямоугольника: {rectangle.area}, Периметр прямоугольника: {rectangle.perimeter}')
        return True


def send_review(review):
    url = "https://review-accept-mrkekovich.vercel.app/"

    data = urllib.parse.urlencode({'review': review}).encode('utf-8')

    request = urllib.request.Request(url, data=data, method='POST')
    try:
        response = urllib.request.urlopen(request)
        print("Данные успешно отправлены!")
    except urllib.error.URLError as e:
        print("Ошибка при отправке данных:", e.reason)


def validate_input(string):
    while isinstance(string, str):
        try:
            return int(string)
        except ValueError:
            string = input('Введите целое число: ')

print("Загрузка...")
loading_animation()
print("""
Готово!

Задания:
1. Реверс строки
2. Отправка отзыва
3. Стоимость билета
4. Площадь прямоугольника
5. Площадь и периметр прямоугольника
""")

task = input('Введите номер задания: ')

while task_manager(task):
    print("""
    Задания:
    1. Реверс строки
    2. Отправка отзыва
    3. Стоимость билета
    4. Площадь квадрата
    5. Площадь и периметр прямоугольника
    """)
    task = input('Введите номер задания: ')
