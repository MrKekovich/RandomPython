task1 = """
1. Написать программу, позволяющую пользователю вводить целые числа до тех пор, пока не будет введено значение 0.
Необходимо определить, сколько пользователь ввел уникальных чисел и вывести результат на экран.
Используйте множество.
"""


def unique_numbers():
    numbers = set()  # создаем множество
    while True:  # бесконечный цикл
        number = int(input("Введите число: "))  # получаем число
        if number == 0:  # если 0, то выход из цикла
            break
        numbers.add(number)  # добавляем в множество (Если такое число есть, то ничего не добавится)
    print(len(numbers))  # выводим количество уникальных чисел


task2 = """
2. Написать программу, позволяющую пользователю ввести код активации.
Программа должна проверить, был ли этот код использован ранее.
Если код уже использовался - вывести строку “Данный код уже был использован”,
иначе вывести “Продукт активирован”. Необходимо использовать множества.
"""


def activation_codes():
    codes = set()  # создаем множество
    while True:  # бесконечный цикл
        code = input("Введите код активации: ")  # получаем код
        if code == "0":  # если 0, то выход из цикла
            break
        if code in codes:
            print("Данный код уже был использован")
        else:
            print("Продукт активирован")
            codes.add(code)  # добавляем в множество (Если такой код есть, то ничего не добавится)


task3 = """
3. Написать программу, позволяющую пользователю ввести текст. 
Слова в тексте разделены одним или несколькими пробелами, или переносом строки. 
Программа должна вывести на экран количество повторений для каждого слова в этом тексте. Используйте словарь.
"""


def frequency_dictionary():
    text = input("Введите текст: ").lower()  # приводим все буквы к нижнему регистру
    words = text.split()  # разделяем текст на слова

    word_count = {}  # создаем пустой словарь

    for word in words:
        if word not in word_count:  # если слово ещё не в словаре
            word_count[word] = 1  # добавляем новое слово в словарь со значением 1
        else:
            word_count[word] += 1  # увеличиваем значение уже существующего слова на 1

    # выводим результат ключ, значение
    for word, count in word_count.items():
        print(word, ":", count)


while True:
    print(task1, task2, task3)
    ask_task = input('Введите номер задания: ')
    if ask_task == '1':
        unique_numbers()  # используем код
    elif ask_task == '2':
        activation_codes()
    elif ask_task == '3':
        frequency_dictionary()
