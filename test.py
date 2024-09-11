value = 'Глобальная value'


def outer_function():
    value = 'Локальная value из outer_function()'

    def inner_function():
        value = 'Локальная value из inner_function()'
        print(value)  # Обратились к переменной value.
        # Сперва ищем это имя в локальном пространстве имён,
        # внутри функции inner_function(). Нашли! Печатаем.


outer_function()

# Будет напечатано:
# Локальная value из inner_function()
