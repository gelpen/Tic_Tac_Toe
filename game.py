# game.py

from gameparts import Board

game = Board()
game.display()
game.make_move(1, 1, 'X')
game.make_move(0, 1, 'O')
game.make_move(2, 1, 'X')
print('Ход сделан!')
game.display()
