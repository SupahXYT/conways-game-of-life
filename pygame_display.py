import pygame, Game
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, MOUSEWHEEL

col_bg = (51, 51, 51)
col_border = (153, 153, 153)
col_fill = (229, 229, 229)

class Display():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
        self.display.fill(col_bg)
        self.game = Game.game(25, 25)
        self.paused = True
        self.scale = 1
        self.ox, self.oy = (0, 0)
        self.button = 1
        self.to_flip = True 
        pygame.display.flip()

    def main(self):
        running = True
        while running:
            self.to_flip = True
            events = pygame.event.get()
            if(len(events) > 0):
                for event in events:
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == KEYDOWN:
                        self.on_key_press(event)
                    elif event.type == MOUSEWHEEL:
                        self.on_scroll(event)
                    elif event.type == MOUSEBUTTONDOWN:
                        self.on_mouse_down(event)
                    elif event.type == MOUSEBUTTONUP:
                        self.on_mouse_up()
                    if event.type == MOUSEMOTION:
                        self.on_motion(event)
            else:
                self.to_flip = False

            if(not self.paused):
                self.game.step()
                self.to_flip = True

            self.draw()
            if(self.to_flip):
                pygame.display.flip()
            pygame.time.wait(5)

        pygame.quit()        

    def on_key_press(self, event):
        if(event.key == pygame.K_SPACE):
            self.paused = not self.paused
        elif(event.key == pygame.K_RIGHT):
            self.game.step()

    def on_scroll(self, event):
        if(event.y == 1):
            self.scale += .25
        elif(event.y == -1):
            if(self.scale > 1):
                self.scale -= .25

    def on_mouse_up(self):
        self.button = 0

    def on_mouse_down(self, event):
        self.button = event.button
        if event.button == 1:
            row = int((event.pos[0] - self.ox)/(8*self.scale))
            col = int((event.pos[1] - self.oy)/(8*self.scale))
            self.game.force(row, col)

    def on_motion(self, event):
        if(self.button == 3):
            self.ox += event.rel[0]
            self.oy += event.rel[1]

    def draw(self):
        grid = self.game.grid
        scale = self.scale
        self.display.fill(col_bg)
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                # smh pygame doesn't support floating point values for drawing
                if(grid[row][col]):
                    pygame.draw.rect(self.display, col_fill, pygame.Rect(self.ox + round(row*8*scale), 
                        self.oy + round(col*8*scale), round(scale*8), round(scale*8)))
                    pygame.draw.rect(self.display, col_border, pygame.Rect(self.ox + round(row*8*scale), 
                        self.oy + round(col*8*scale), round(scale*8), round(scale*8)), round(scale))
                else:
                    pygame.draw.rect(self.display, col_bg, pygame.Rect(self.ox + round(row*8*scale), 
                        self.oy + round(col*8*scale), round(scale*8), round(scale*8)))
                    pygame.draw.rect(self.display, col_border, pygame.Rect(self.ox + round(row*8*scale), 
                        self.oy + round(col*8*scale), round(scale*8), round(scale*8)), round(scale))

   
d = Display()
d.main()
