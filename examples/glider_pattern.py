if __name__ == "__main__":
    # Initialize a 10x10 grid
    game = GameOfLife(10, 10)

    # Set up a simple glider pattern
    glider = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    for row, col in glider:
        game.set_cell(row, col, 1)

    # Run the simulation for 10 generations
    for _ in range(10):
        game.display()
        game.next_generation()
