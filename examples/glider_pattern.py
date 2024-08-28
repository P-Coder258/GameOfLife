from game_of_life import GameOfLife

game = GameOfLife(10, 10)
glider = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
for row, col in glider:
    game.set_cell(row, col, 1)

for _ in range(10):
    game.display()
    game.next_generation()

