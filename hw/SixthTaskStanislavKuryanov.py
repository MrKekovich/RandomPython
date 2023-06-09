from sympy import primerange  # импорт модуля


def validate_input(promt, type):
    """
    Функция просит ввести данные и конвертировать их в type.
    Пока это не получится функция будет предлагать ввести данные еще раз.
    """
    while True:
        user_input = input(promt)
        try:
            return type(user_input)
        except Exception as e:
            print(f"Ошибка! {e}")


task1 = """
Напишите функцию get_primes_from_range(start, end), которая принимает два натуральных числа star, end
и возвращает список всех простых чисел от start до end.
"""


def get_primes_from_range(start, end):
    return list(primerange(start, end))
    # сейчас просто поймите то, что list(primerange(start, end)) возвращает список простых чисел. Вникать не надо.


task2 = """
Напишите функцию get_season_by_month(month), которая принимает натуральное число month 
и возвращает название времени года.
"""


def get_season_by_month(month):
    if month in (1, 2, 12):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Неизвестный месяц"


def main():
    """
    Основная функция.
    Даёт выбрать задачу и использует существующие функции.
    """
    while True:
        task = input("Введите задачу: ")
        if task == "exit":
            break
        elif task == '1':
            start = validate_input("Введите начало диапазона: ", int)
            end = validate_input("Введите конец диапазона: ", int)
            print(f'Простые числа от {start} до {end}: \n{get_primes_from_range(start, end)}')
        elif task == '2':
            month = validate_input("Введите месяц: ", int)
            print(get_season_by_month(month))


main()