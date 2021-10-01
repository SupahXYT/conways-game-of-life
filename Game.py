def conway(self, snapshot, row, col):
    neighbors = self.neighbors(snapshot, row, col)

    if(snapshot[row][col]): # if alive
        if(neighbors < 2 or neighbors > 3):
            self.grid[row][col] = False
    else: # if dead
        if(neighbors == 3):
            self.grid[row][col] = True

class game:

    def __init__(self, width, height, act):
        self.steps = 0
        self.grid = [[False for i in range(height)] for j in range(width)]
        self.act = act

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
                self.grid[row][col] = self.act(snapshot, row, col)

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

class act():
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

#     def __call__(self, snapshot, row, col):
#         neighbors = game.neighbors(snapshot, row, col)

        # if(snapshot[row][col]): # if alive
        #     if(neighbors < self.lower or neighbors > self.upper):
        #         return False
        # else: # if dead
        #     if(neighbors == 3):
        #         return True

    def __call__(self, snapshot, row, col):
        neighbors = game.neighbors(snapshot, row, col)
        if(snapshot[row][col]): # if alive
            if(neighbors < self.lower):
                return False
            elif(neighbors < self.upper):
                return snapshot[row][col]
            else:
                return False
        else: # if dead
            if(neighbors == self.upper - self.lower + 1):
                return True
