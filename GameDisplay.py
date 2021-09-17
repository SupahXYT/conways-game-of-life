import gi
import Game
from random import randrange

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

class GameDisplay:

    def __init__(self):
        self.window = Gtk.Window(title="Conway's Game of Life")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_default_size(450, 550)
        self.window.set_border_width(5)

        width = 40
        height = 40 

        self.game = Game.Game(width, height)


        self.drawingarea = Gtk.DrawingArea()
        self.frame = Gtk.Frame()
        self.frame.set_label("John Conway's Game of Life")
        self.frame.add(self.drawingarea);
        self.window.add(self.frame);
        self.drawingarea.connect('draw', self.draw)
        self.window.show()
        self.frame.show()
        self.drawingarea.show()
        GObject.timeout_add(100, self.update) 

    def draw(self, da, ctx):
        self.game.step()

        bwidth, bheight = (8, 8)

        grid = self.game.getgrid()

        # I hate python lists so much
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                ctx.rectangle(row*bwidth, col*bheight, bwidth, bheight)
                if(grid[row][col]):
                    ctx.set_source_rgb(.9, .9, .9)
                    ctx.fill_preserve()
                    ctx.set_source_rgb(0.6, 0.6, 0.6)
                    ctx.set_line_width(2)
                    ctx.stroke()
                else:
                    ctx.set_source_rgb(0.6, 0.6, 0.6)
                    ctx.set_line_width(2)
                    ctx.stroke()

        return True

    def update(self):
        self.drawingarea.queue_draw()
        return True

    def main(self):
        Gtk.main()

run = GameDisplay()
run.main()

