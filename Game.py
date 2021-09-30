def conway(self, snapshot, row, col):
    neighbors = self.neighbors(snapshot, row, col)

    if(snapshot[row][col]): # if alive
        if(neighbors < 2 or neighbors > 3):
            self.grid[row][col] = False
    else: # if dead
        if(neighbors == 3):
            self.grid[row][col] = True

class game:

    def __init__(self, width, height, rule):
        self.steps = 0
        self.grid = [[False for i in range(height)] for j in range(width)]
        self.act = rule

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

    @staticmethod
    def adjneighbors(grid, row, col): 

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

        return neighbors

    def step(self):
        # snapshot = grid does NOT work
        snapshot = [row[:] for row in self.grid]

        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[row])):
                self.act(self, snapshot, row, col)

        print(f'step: {self.steps}')
        self.steps += 1
    
    def getgrid(self):
        return self.grid

    def get_pop(self):
        pop = 0
        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[row])):
                if(self.grid[row][col]):
                    pop += 1

        return pop

    def force(self, row, col):
        self.grid[row][col] = not self.grid[row][col]

class boundgame(game):
    def __init__(self, width, height, lower, upper):
        self.lower = lower
        self.upper = upper
        rule = self.rule
        super().__init__(width, height, rule)

    def rule(self, snapshot, row, col):
        if(snapshot[row][col]): # if alive
            if(self.neighbors(snapshot, row, col) < self.lower):
                self.grid[row][col] = False
            elif(self.neighbors(snapshot, row, col) < self.upper):
                pass
            else:
                self.grid[row][col] = False
        else: # if dead
            if(self.neighbors(snapshot, row, col) == 3):
                self.grid[row][col] = True
    
    def neighbors(self, grid, row, col):
        super().neighbors(grid, row, col)

    def step(self):
        super().step()

    def force(self, row, col):
        super().force(row, col)


