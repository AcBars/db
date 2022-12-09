import request_db

def start(name):
    print(f'Здравствуйте {name}!\n Вас приветствует база данных СНТ "Садовод".\n Я умею:\n 1. Добовлять в базу новых членов СНТ.')
    print(' 2. Добовлять в базу участки.\n 3. Показывать список участков и их владельцев')
    pt = int(input('Для дальнейшей работы с базой укажите введите номер пункта действия которое вы хотите выполнить: '))
    if pt == 1:
        request_db.add_person(int(input('Введите номер участка: ')))
    elif pt == 2:
        request_db.add_plot()
    elif pt == 3:
        request_db.select()