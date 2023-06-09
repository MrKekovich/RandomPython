import tempfile
import urllib.request
from abc import ABC, abstractmethod
from tkinter import *
from PIL import Image

ascii_logo = r"""

  __  __          _  __         _                      _          _     
 |  \/  |        | |/ /        | |                    (_)        | |    
 | \  / |  _ __  | ' /    ___  | | __   ___   __   __  _    ___  | |__  
 | |\/| | | '__| |  <    / _ \ | |/ /  / _ \  \ \ / / | |  / __| | '_ \ 
 | |  | | | |    | . \  |  __/ |   <  | (_) |  \ V /  | | | (__  | | | |
 |_|  |_| |_|    |_|\_\  \___| |_|\_\  \___/    \_/   |_|  \___| |_| |_|
                                                                                                                       
"""


# Singleton -----------------------------------------------------------------------------------------------
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        it = cls.__dict__.get('__it__')
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwargs)
        return it

    def init(self, *args, **kwargs):
        pass


# -----------------------------------------------------------------------------------------------------------


# Windows ---------------------------------------------------------------------------------------------------
# Extra windows ---------------------------------------------------------------------------------------------
class ErrorWindow(Toplevel):
    def __init__(self, error):
        super().__init__()

        self.title("Ошибка")
        self.geometry("500x125")

        error_label = Label(self, text=f"Произошла ошибка: {error}")
        error_label.pack()

        ok_button = Button(self, text="OK", command=self.destroy)
        ok_button.pack()


class ExtraWindow(ABC, Toplevel):
    def __init__(self):
        super().__init__()

    @staticmethod
    def error_message(error):
        error_window = ErrorWindow(error)

class TaskMenu(ExtraWindow):
    def __init__(self):
        super().__init__()
        self.task_button1 = Button(self, text='Задание 1', command=self.task1)
        self.task_button2 = Button(self, text='Задание 2', command=self.task2)
        self.task_button3 = Button(self, text='Задание 3', command=self.task3)
        self.task_button4 = Button(self, text='Задание 4', command=self.task4)

        self.task_button1.pack()
        self.task_button2.pack()
        self.task_button3.pack()
        self.task_button4.pack()

    @staticmethod
    def task1():
        FirstTaskWindow()

    @staticmethod
    def task2():
        SecondTaskWindow()

    @staticmethod
    def task3():
        ThirdTaskWindow()

    @staticmethod
    def task4():
        FourthTaskWindow()


class TaskWindow(ExtraWindow, ABC):
    def __init__(self, task_number):
        super().__init__()
        self.geometry('800x400')

        self.title(f'Задание {task_number}')

        self.description = Label(self)

        self.text_area = Text(self, height=10, width=72)

        self.result_button = Button(self, text='Результат', command=self.result)

        self.result_text = Label(self, text=f'Результат: ')

        self.error_text = Label(self, text='')

        self.description.pack()
        self.text_area.pack()
        self.result_button.pack()
        self.result_text.pack()

    @abstractmethod
    def result(self):
        pass


class FirstTaskWindow(TaskWindow):

    def __init__(self):
        super().__init__(1)
        self.text_description = """
        Написать программу, позволяющую пользователю вводить целые числа до тех пор,
        пока не будет введено значение 0. Необходимо определить, сколько пользователь ввел уникальных чисел
        и вывести результат на экран. Используйте множество.
        """

        self.description.configure(text=self.text_description)

        self.numbers = set()

        self.submit_button = Button(self, text='Записать', command=self.submit)

        self.input_numbers = Text(self, height=1, width=72, state='disabled')

        self.submit_button.pack(before=self.result_button)
        self.input_numbers.pack(before=self.result_text)

    def submit(self):
        text = self.text_area.get(index1='1.0', index2=END)
        try:
            number = int(text)
            self.numbers.add(number)
            self.input_numbers.configure(state='normal')
            self.input_numbers.insert("1.0", f'{number}, ')
            self.input_numbers.configure(state='disabled')
            self.text_area.delete(1.0, END)
        except Exception as e:
            self.error_message(e)

    def result(self):
        self.text_area.delete(1.0, END)
        self.result_text.configure(text=f'Результат: {len(self.numbers)} уникальное(ых) число(а).')
        self.numbers = set()
        self.input_numbers.configure(state='normal')
        self.input_numbers.delete("1.0", END)
        self.input_numbers.configure(state='disabled')


class SecondTaskWindow(FirstTaskWindow):
    def __init__(self):
        super().__init__()

        self.title(f'Задание 2')

        self.text_description = """
        Написать программу, позволяющую пользователю ввести код активации.
        Программа должна проверить, был ли этот код использован ранее.
        Если код уже использовался - вывести строку “Данный код уже был использован”,
        “Продукт активирован” - иначе. Необходимо использовать множества.
        """

        self.description.configure(text=self.text_description)

        self.submit_button.destroy()

        self.input_numbers.destroy()

        self.codes = set()

    def result(self):
        code = self.text_area.get(index1='1.0', index2=END)
        self.text_area.delete(1.0, END)
        try:
            self.result_text.configure(text=f'Результат: {self.find_code(code)}')
        except Exception as e:
            print(e)
        self.codes.add(code)

    def find_code(self, code):
        if code == '':
            raise Exception('Введите код')
        elif code in self.codes:
            return 'Данный код уже был использован'
        else:
            return 'Продукт активирован'


class ThirdTaskWindow(TaskWindow):
    def __init__(self):
        super().__init__(2)

        self.title(f'Задание 3')

        self.text_description = """
        Написать программу, позволяющую пользователю ввести текст.
        Слова в тексте разделены одним или несколькими пробелами, или переносом строки. 
        Программа должна вывести на экран количество повторений для каждого слова в этом тексте.
        Используйте словарь.
        """

        self.description.configure(text=self.text_description)

    @staticmethod
    def frequency_dictionary(text=''):
        words = text.split()

        word_count = {}

        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

        return word_count

    def result(self):
        text = self.text_area.get(index1='1.0', index2=END)
        self.text_area.delete(1.0, END)
        self.result_text.configure(text=f'Результат: \n{self.frequency_dictionary(text)}')


class FourthTaskWindow(ThirdTaskWindow):
    def __init__(self):
        super().__init__()

        self.title(f'Задание 4')

        self.text_description = """
        (Задача по желанию)
        Написать программу, позволяющую пользователю ввести текст. 
        Слова в тексте разделены одним или несколькими пробелами, или переносом строки. 
        Программа должна вывести на экран самое часто встречающееся слово. 
        Используйте словарь.
        """

        self.description.configure(text=self.text_description)

    def result(self):
        text = self.text_area.get(index1='1.0', index2=END)
        self.text_area.delete(1.0, END)
        frequency_dict = self.frequency_dictionary(text)
        max_item = max(frequency_dict.items(), key=lambda x: x[1])
        self.result_text.configure(text=f'Результат: \n{max_item} \nСловарь: \n{frequency_dict}')


# ----------------------------------------------------------------------------------------------------------
class Window(Tk, Singleton):  # Main window

    def init(self):
        super().__init__()
        self.label = Label(self, text='Пятое ДЗ Станислав Курянов')
        self.logo = Text(self, height=10, width=72)
        self.logo.insert("1.0", ascii_logo)
        self.logo.configure(state="disabled")
        # self.animate = Button(self, text='Загрузить GIF', command=self.load_logo)
        # self.animate.pack()  не работает... ну и фиг с ним. Может потом разберусь
        self.button = Button(self, text='Меню заданий', command=self.create_menu)
        self.label.pack()
        self.logo.pack()
        self.button.pack()

    def __init__(self):
        self.current_frame = 0
        self.delay = 50
        self.animate = None
        self.art = None
        self.logo_data = None
        self.button = None
        self.label = None
        self.logo = None
        self.error_message = None
        self.logo_gif = None

    def load_logo(self):
        try:
            self.get_logo()
            canvas = Canvas(self, width=self.logo_gif.width(), height=self.logo_gif.height())
            canvas.pack()
            # self.animate_gif(canvas)
        except Exception as e:
            self.error_message = Label(self, text=f'Не удалось загрузить картинку, ошибка: {e}.')
            self.error_message.pack()

    def get_logo(self):
        self.logo_data = urllib.request.urlopen('https://imgur.com/ni0uvv2.gif').read()
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(self.logo_data)
            gif_info = Image.open(f)
            self.logo_gif = [PhotoImage(file=f.name, format=f'gif -index {i}') for i in range(gif_info.n_frames)]

    def create_menu(self):
        menu = TaskMenu()
        # def animate_gif(self, canvas):
    #     canvas.create_image(0, 0, image=self.logo_gif[self.current_frame], anchor='nw')
    #     self.current_frame = (self.current_frame + 1) % len(self.logo_gif)
    #     self.after(self.delay, lambda: self.animate_gif(canvas))


# -----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = Window()
    app.title('Пятое ДЗ')
    app.geometry('1024x1024')
    app.mainloop()
