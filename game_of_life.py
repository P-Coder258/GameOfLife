class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, row, col, state):
        #Set the state of a specific cell.
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = state

    def display(self):
        # Display the current grid.
        for row in self.grid:
            print(" ".join("█" if cell else " " for cell in row))
        print("\n" + "-" * (self.cols * 2))

    def count_neighbors(self, row, col):
        #Count the number of live neighbors around a specific cell.
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count

    def next_generation(self):
        # Compute the next generation of the grid.
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = self.count_neighbors(row, col)
                if self.grid[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[row][col] = 0  # Cell dies
                    else:
                        new_grid[row][col] = 1  # Cell survives
                else:
                    if live_neighbors == 3:
                        new_grid[row][col] = 1  # Cell is born
        self.grid = new_grid
