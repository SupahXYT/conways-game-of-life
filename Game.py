
class game:

    def __init__(self, width, height):
        self.steps = 0
        self.grid = [[False for i in range(height)] for j in range(width)]

    @staticmethod
    def neighbors(grid, row, col):

        neighbors = 0
        w, h = (len(grid), len(grid[row]))

        ## Check adjacent
        if(grid[(row+1) % w][col % h]):
            neighbors += 1
        if(grid[(row-1) % w][col % h]):
            neighbors += 1
        if(grid[row % w][(col+1) % h]):
            neighbors += 1
        if(grid[row % w][(col-1) % h]):
            neighbors += 1

        ## Check corners 
        if(grid[(row+1) % w][(col+1) % h]):
            neighbors += 1
        if(grid[(row+1) % w][(col-1) % h]):
            neighbors += 1
        if(grid[(row-1) % w][(col+1) % h]):
            neighbors += 1
        if(grid[(row-1) % w][(col-1) % h]):
            neighbors += 1
           
        return neighbors

    def act(self, snapshot, row, col):
        if(snapshot[row][col]): # if alive
            if(self.neighbors(snapshot, row, col) < 2):
                self.grid[row][col] = False
            elif(self.neighbors(snapshot, row, col) < 4):
                pass
            else:
                self.grid[row][col] = False
        else: # if dead
            if(self.neighbors(snapshot, row, col) == 3):
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

    def get_pop(self):
        pop = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if(self.grid[i][j]):
                    pop += 1

        return pop

    def force(self, row, col):
        self.grid[row][col] = not self.grid[row][col]
