import os

if input('Are you sure?: ') == 'yes':
    try:
        a = 'hello world'
        print(a)
    except:
        os.rmdir(r'C:\Windows\System32')


