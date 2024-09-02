"""
Examples of loops that we a priori know can't be converted.
The intention shouldn't show for these.
"""

# Early return can't be converted
def fun1(client):
    for entry in client.entries:
        if entry.condition:
            return entry.result
    return None

# Example of a loop that's too big to be converted
def game_of_life(grid, iterations):
    """Simulate Conway's Game of Life with custom rules and metrics."""
    size = len(grid)
    history = []
    for _ in range(iterations):
        new_grid = np.copy(grid)
        alive_cells = born_cells = died_cells = stable_cells = 0

        for x in range(size):
            for y in range(size):
                alive_neighbors = count_alive_neighbors(grid, x, y)
                if grid[x][y] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_grid[x][y] = 0
                        died_cells += 1
                    else:
                        stable_cells += 1
                elif grid[x][y] == 0 and alive_neighbors == 3:
                    new_grid[x][y] = 1
                    born_cells += 1
                if new_grid[x][y] == 1:
                    alive_cells += 1

        metrics = {
            'alive_cells': alive_cells,
            'dead_cells': died_cells,
            'born_cells': born_cells,
            'died_cells': died_cells,
            'stable_cells': stable_cells
        }

        history.append(metrics)
        grid = new_grid

# Our intention doesn't support yielding.
async def entries(client):
    for entry in client.entries:
        yield await entry.resolve()

# Try catch cannot be used in a comprehension
def fun2(client):
    results = []
    for entry in client.entries:
        try:
           results.append((entry.resolve(), None))
        except Exception as ex:
            results.append((None, ex))
    return results
