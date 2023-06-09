class RandomClass:
    numbers = []

    def __init__(self, num_list):
        try:
            for i in num_list:
                self.numbers.append(int(i))
        except Exception as e:
            print(e)

    def summ(self):
        try:
            return sum(self.numbers)
        except Exception as e:
            print(e)


user_input = input('Enter numbers: ').split(' ')

execute = RandomClass(user_input)
print(execute.summ())

