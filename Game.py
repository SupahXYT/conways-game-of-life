
def neighbors(grid, row, col):
    neighbors = 0

    if(row != 0 and row < len(grid) - 2 and col != 0 and col < 39):

        if(grid[row+1][col]):
            print("row+1 col")
            neighbors += 1
        if(grid[row-1][col]):
            print("row-1 col")
            neighbors += 1
        if(grid[row][col+1]):
            print("row col+1")
            neighbors += 1
        if(grid[row][col-1]):
            print("row col-1")
            neighbors += 1

        ## Check corners 
        if(grid[row+1][col+1]):
            print("row+1 col+1")
            neighbors += 1
        if(grid[row+1][col-1]):
            print("row+1 col-1")
            neighbors += 1
        if(grid[row-1][col+1]):
            print("row-1 col+1")
            neighbors += 1
        if(grid[row-1][col-1]):
            print("row-1 col-1")
            neighbors += 1

    if(neighbors > 0):
        print(f'neighbor {neighbors}')

    return neighbors

class Game:

    def __init__(self, width, height):
        self.steps = 0
        self.grid = [[False for i in range(height)] for j in range(width)]
        self.grid[3][6] = True
        self.grid[4][6] = True
        self.grid[5][6] = True
        print(len(self.grid[0]))

    def act(self, snapshot, row, col):
        if(snapshot[row][col]): # if alive
            if(neighbors(snapshot, row, col) < 2):
                print("die")
                self.grid[row][col] = False
            elif(neighbors(snapshot, row, col) < 4):
                pass
            else:
                print("die")
                self.grid[row][col] = False
        else: # if dead
            if(neighbors(snapshot, row, col) == 3):
                print("populate")
                self.grid[row][col] = True

    def step(self):
        snapshot = self.grid.copy()

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.act(snapshot, i, j)

        print(f'steps; {self.steps}')
        self.steps += 1
    
    def getgrid(self):
        return self.grid


