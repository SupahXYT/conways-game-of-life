
class cell:

    def __init__(self, plane, state):
        self.plane = plane
        self.isalive = state
        self.color = [0, 0, 0]
    
    def act(self, row, col):
        neighbors = 0

        if(self.plane[row + 1][col]):
            neighbors += 1
        if(self.plane[row - 1][col]):
            neighbors += 1

    def getcolor(self):
        return self.color
        
    
    
