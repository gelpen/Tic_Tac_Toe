# def calc(func, first, second, tchert):
#     return func(first, second, tchert)


# # Первый аргумент при вызове calc() - это лямбда-функция с нужным выражением:
# print(calc(lambda a, b, c: a + b + c, 5, 10, 20))   # Складываем.
# print(calc(lambda a, b, c: a * b * c, 30, 10, 20))  # Умножаем.
# print(calc(lambda a, b, c: (a ** b) ** c, 30, 2, 20))  # Возводим в степень.

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func, sequence):
    for item in sequence:
        func(item)


# Этот вызов для каждого имени из списка должен напечатать
# строчку Привет, <имя>!
say_to_all(lambda a: print(f'Здравствуй, {a}!') if a[0] =='С' else print(f'Привет, {a}!'), people)
