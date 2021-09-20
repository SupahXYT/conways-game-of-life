def check(buf, grid, row, col):
    neighbors = buf;
    if(grid[row+1][col]):
        neighbors += 1
    if(grid[row-1][col]):
        neighbors += 1
    if(grid[row][col+1]):
        neighbors += 1
    if(grid[row][col-1]):
        neighbors += 1

    ## Check corners 
    if(grid[row+1][col+1]):
        neighbors += 1
    if(grid[row+1][col-1]):
        neighbors += 1
    if(grid[row-1][col+1]):
        neighbors += 1
    if(grid[row-1][col-1]):
        neighbors += 1

    return neighbors

def neighbors(grid, row, col):
    neighbors = 0

    if(row != 0 and row < len(grid) - 2 and col != 0 and col < 39):
        neighbors = check(neighbors, grid, row, col)
        
    return neighbors

class Game:

    def __init__(self, width, height):
        self.steps = 0
        self.grid = [[False for i in range(height)] for j in range(width)]
        self.grid[20][20] = True
        self.grid[21][20] = True
        self.grid[22][20] = True
        self.grid[21][19] = True
        self.grid[21][18] = True
        self.grid[21][17] = True
        self.grid[21][16] = True
        print(len(self.grid[0]))

    def act(self, snapshot, row, col):
        if(snapshot[row][col]): # if alive
            if(neighbors(snapshot, row, col) < 2):
                self.grid[row][col] = False
            elif(neighbors(snapshot, row, col) < 4):
                pass
            else:
                self.grid[row][col] = False
        else: # if dead
            if(neighbors(snapshot, row, col) == 3):
                self.grid[row][col] = True

    def step(self):
        # snapshot = grid does NOT work
        snapshot = [row[:] for row in self.grid]

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.act(snapshot, i, j)

        print(f'step: {self.steps}')
        self.steps += 1
    
    def getgrid(self):
        return self.grid


