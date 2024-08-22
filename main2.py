HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выйти из программы.
"""

today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(today, tomorrow, other)
    elif command == "add":
        data = input('Введите дату: ')
        task = input("Введите название задачи: ")
        if data == 'Сегодня':
            today.append(task)
        elif data == 'Завтра':
            tomorrow.append(task)
        else:
            other.append(task)

        print("Задача добавлена")

    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print("Неизвестная команда")

print("До свидания")
