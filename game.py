
def neighbors(grid, row, col):
    neighbors = 0
    return neighbors

class Game:

    def __init__(self, width, height):
        self.grid = [[]]
        self.steps = 0

        for i in range(0, width):
            for j in range(0, height):
                self.grid[i][j].append(False)

    def act(self, snapshot, row, col):
        if(snapshot[row][col]): # if alive
            if(neighbors(snapshot, row, col) < 2):
                self.grid[row][col] = False
            elif(neighbors(snapshot, row, col) < 4):
                pass
            else:
                self.grid[row][col] = False
        else: # if dead
            pass

    def step(self):
        snapshot = self.grid

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.act(snapshot, i, j)

        self.steps += 1
    


