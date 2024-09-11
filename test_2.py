# Импортируйте необходимые модули.
from datetime import datetime
# date_object = datetime.strptime(date_str, "%d.%m.%Y")

# Укажите два параметра функции:


def validate_record(name, date_birth):
    # Напишите код, верните булево значение.
    try:
        datetime.strptime(date_birth, "%d.%m.%Y")
        return True
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {date_birth}')
        return False


# Укажите параметры функции:
def process_people(data):
    # Объявите счётчики.
    good_count = 0
    bad_count = 0
    for i in data:
        name, date_birth = i
        if validate_record(name, date_birth):
            good_count += 1
        else:
            bad_count += 1
    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.
    print(f'Корректных записей: {good_count}')
    print(f'Некорректных записей: {bad_count} ')
    result = {"good": good_count, "bad": bad_count}
    return result


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
# Корректных записей: <число>
# Некорректных записей: <число>
