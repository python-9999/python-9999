def add():
    print('command or "exit".')
    while True:
       i = input('>>>')

       if i == 'add+':
           a, b = int(input('num 1: ')), int(input('num 2: '))
           print(f'={a+b}')

       elif i == 'add*':
           a, b = int(input('num 1: ')), int(input('num 2: '))
           print(f'={a*b}')

       elif i == 'help':
           print('command (3):\nadd+\nadd*\nexit')

       elif i == 'exit':
           break

try:  
    user_input = int(input('1.add\n>>>'))
    if user_input == 1:
        add()
    elif user_input == '0':
        pass
    else:
        print('ошибка. (внутри блока user_input)')
except ValueError:
    print('ошибка.')