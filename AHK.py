import pyautogui
import time
import math
import numpy as np


def delay(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass


delay(1)

width, height = pyautogui.size()
pyautogui.PAUSE = 0
t = np.linspace(-12 * math.pi, 32 * math.pi, 3000)
x = np.cos(t) * 200 + pyautogui.position()[0]  # добавляем текущую позицию курсора
y = np.sin(t) * np.cos(t) * 200 + pyautogui.position()[1]

for i in range(len(x)):
    pyautogui.moveTo(x[i], y[i])
    delay(0.0001)
