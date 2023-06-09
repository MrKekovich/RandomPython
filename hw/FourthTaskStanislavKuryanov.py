from abc import ABC, abstractmethod


class ReverseList:
    def __init__(self, some_list):
        self.some_list = some_list

    @property
    def reverse_list(self):
        return self.some_list[::-1]


class MaxMinAvg:
    def __init__(self):
        self.some_list = []

    def set_number(self, number):
        self.some_list.append(number)

    @property
    def max_value(self):
        return max(self.some_list)

    @property
    def min_value(self):
        return min(self.some_list)

    @property
    def avg_value(self):
        return sum(self.some_list) / len(self.some_list)


class SubstringChecker:
    def __init__(self, string, substring):
        self.string = string
        self.substring = substring

    def has_substring(self):
        return self.string.count(self.substring) > 0


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

    @staticmethod
    def print_menu():
        print("\nМеню:")
        print("1 - Поиск подстроки в строке")
        print("2 - Вывод списка в обратном порядке")
        print("3 - Максимальное, минимальное и среднее значение")
        print("0 - Выход из программы")

    @staticmethod
    def search_substring():
        user_string = input("Введите строку: ")
        user_substring = input("Введите подстроку: ")
        substring_checker = SubstringChecker(user_string, user_substring)
        if substring_checker.has_substring():
            print(f'Есть контакт!')
        else:
            print(f'Мимо!')

    @staticmethod
    def print_list_in_reverse(some_list=None):
        reverse_list = ReverseList(some_list or ['a', 'b', 'c', 'd', 'e'])
        print(f'оригинальный список {reverse_list.some_list}')
        print(f'перевёрнутый список {reverse_list.reverse_list}')

    @staticmethod
    def max_min_avg():
        max_min_avg = MaxMinAvg()
        while True:
            user_input = Utils.get_valid_input('Введите число:', int)
            if user_input == 0:
                break
            max_min_avg.set_number(user_input)
        print(f'Максимальное значение: {max_min_avg.max_value}')
        print(f'Минимальное значение: {max_min_avg.min_value}')
        print(f'Среднее значение: {max_min_avg.avg_value}')

    @staticmethod
    def tasks():
        while True:
            Utils.print_menu()
            choice = Utils.get_valid_input("Выберите задачу: ", int)
            if choice == 0:
                break
            elif choice == 1:
                Utils.search_substring()
            elif choice == 2:
                choice = input("Ввести список вручную? (y/n): ")
                if choice == 'y':
                    Utils.print_list_in_reverse(input("Введите эелементы списка через пробел: ").split(' '))
                else:
                    Utils.print_list_in_reverse()
            elif choice == 3:
                Utils.max_min_avg()
            else:
                print("Некорректный выбор. Попробуйте еще раз.")


def main():
    Utils.tasks()


if __name__ == '__main__':
    main()
