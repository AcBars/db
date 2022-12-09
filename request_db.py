import sqlite3

def add_person(number):
    db = sqlite3.connect('basedata.db')
    cur = db.cursor()
    cur.execute("SELECT Number_plot FROM Plot")
    result = cur.fetchall()
    count = 0
    for i in range(len(result)):
        if number == result[i][0]:
            surname = input('Введите фамилию владельца участка: ')
            name = input('Введите имя владельца участка: ')
            middle_name = input(('Введите отчество владельца участка: '))
            cur.execute("INSERT INTO person ('Surname', 'Name', 'Middle_name') VALUES ('%s', '%s', '%s')" %(surname, name, middle_name))
            db.commit()
            count += 1
    if count == 1:
        cur.execute("SELECT id FROM person")
        temp = cur.fetchall()
        id_person = temp[len(temp) - 1][0]
        cur.execute("UPDATE Plot SET owner=%d WHERE Number_plot=%d" % (id_person, number))
        db.commit()
        print(f'Данные владельца участка №{number} внесены в базу.')
    else: print(f'Участок с №{number} отсутствует. Внесите участок №{number} в базу.')
    db.close()

def add_plot():
    db = sqlite3.connect('basedata.db')
    cur = db.cursor()
    number_plot = int(input('Введите номер участка: '))
    land_area = int(input('Введите площадь участка в квадратных метрах: '))
    number_cadastr = input('Введите кадастровый номер участка: ')
    cur.execute("INSERT INTO Plot ('Number_plot', 'Land_area', 'Number_cadastr') VALUES (%d, %d, '%s')" %(number_plot, land_area, number_cadastr))
    db.commit()
    db.close()
    db = sqlite3.connect('basedata.db')
    cur = db.cursor()
    cur.execute("INSERT INTO person ('Number_plot') VALUES (%d)" % (number_plot))
    db.commit()
    db.close()
    print(f'Участок №{number_plot} успешно добавлен в базу.')

def select():
    db = sqlite3.connect('basedata.db')
    cur = db.cursor()
    cur.execute("SELECT Number_plot, Land_area, Number_cadastr, owner FROM Plot")
    result = cur.fetchall()
    for i in range(len(result)):
        temp = result[i]
        print(f'{i + 1}. Участок №{temp[3]} - владелец {temp[0]} {temp[1]} {temp[2]}, площадь участка {temp[4]}кв.м, кадастровый номер: {temp[5]}')
    db.close()
