text = input('Enter your text: ')
user_input = ' '
while user_input != '!EXIT':
    user_input = input('')
    text += user_input
try:
    print(len(user_input.split()))
except Exception as e:
    print(f'Error {e}')