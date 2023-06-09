from tkinter import *
from PIL import Image, ImageTk

# Создание окна приложения
root = Tk()

# Загрузка GIF-изображения
gif_image = Image.open("Wow-gif.gif")

# Преобразование изображения для использования в Tkinter
tk_image = ImageTk.PhotoImage(gif_image)

# Создание виджета Label с изображением
label = Label(root, image=tk_image)
label.pack()

# Запуск главного цикла обработки событий
root.mainloop()