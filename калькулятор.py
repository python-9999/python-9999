def add():
    print('command or "exit".')
    while True:
       user_input = input('>>>')

       if user_input == 'add+':
           a, b = int(input('num 1: ')), int(input('num 2: '))
           print(f'={a+b}')

       elif user_input == 'add*':
           a, b = int(input('num 1: ')), int(input('num 2: '))
           print(f'={a*b}')

       elif user_input == 'help':
           print('command (3):\nadd+\nadd*\nexit')

       elif user_input == 'exit':
           break

try:  
    user_input2 = int(input('1.add\n>>>'))
    if user_input2 == 1:
        add()
    elif user_input2 == '0':
        pass
    else:
        print('ошибка. (внутри блока user_input)')
except ValueError:
    print('ошибка.')
