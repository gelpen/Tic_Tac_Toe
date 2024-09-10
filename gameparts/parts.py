# gameparts/parts.py

class Board:
    """Класс, который описывает игровое поле """

    # Новый атрибут.
    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        # Цикл проходится по всем столбцам игрового поля.
        for i in range(self.field_size):
            # А потом по всем строчкам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True
    
    # Этот метод будет определять победу.
    def check_win(self, player):
        # Тут реализована проверка по вертикали и горизонтали.
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        # Тут реализована проверка по диагонали.
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False
    
    def write_result(self, result):
        # file_actions.py
        # Открыть на запись файл example.txt
        file = open('results.txt', 'a', encoding='utf-8') 
        # Записать в файл строку.
        file.write(result + '\n')
        # Закрыть файл.
        file.close()

    # Переопределяем метод __str__.

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{Board.field_size}x{Board.field_size}'
        )
