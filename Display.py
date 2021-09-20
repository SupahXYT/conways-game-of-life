import gi
import Game

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject

class Display(Gtk.Window):
    def __init__(self):
        super().__init__(title="Conway's Game of Life")

        self.set_border_width(5)
        self.set_default_size(1000, 800)

        self.origin_x, self.origin_y = (0, 0)
        self.init_x, self.init_y = (0, 0)
        self.velx, self.vely = (0, 0)
        self.scale = 4
        self.speed = 5
        self.button = 1

        box = Gtk.EventBox()
        box.add_events(Gdk.EventMask.BUTTON_MOTION_MASK)
        box.add_events(Gdk.EventMask.KEY_RELEASE_MASK)
        box.add_events(Gdk.EventMask.SCROLL_MASK)
        box.connect("button-press-event", self.on_click)
        box.connect("motion-notify-event", self.on_motion)
        box.connect("scroll-event", self.on_scroll)

        self.game = Game.Game(50, 50)
        self.count = 0

        frame = Gtk.Frame(label="John Conway's Game of Life")
        self.drawingarea = Gtk.DrawingArea()
        self.drawingarea.connect('draw', self.draw)

        frame.add(self.drawingarea)
        box.add(frame)
        self.add(box)
        GObject.timeout_add(100, self.update) 

    def on_motion(self, widget, event):
        if(self.button == 3):
            velocity_x = event.x - self.init_x
            velocity_y = event.y - self.init_y
            self.origin_x += velocity_x 
            self.origin_y += velocity_y
            self.init_x = event.x
            self.init_y = event.y

    def on_scroll(self, widget, event):
        if(event.direction == Gdk.ScrollDirection.UP):
            self.scale *= 1.1
        elif(event.direction == Gdk.ScrollDirection.DOWN):
            self.scale *= 0.9

    def on_click(self, widget, event):
        self.button = event.button 
        self.init_x = event.x
        self.init_y = event.y

    def draw(self, da, ctx):

        grid = self.game.grid

        # I hate python lists so much
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                ctx.rectangle(self.origin_x+(row*8*self.scale), self.origin_y+(col*8*self.scale), self.scale*8, self.scale*8)
                if(grid[row][col]):
                    ctx.set_source_rgb(.9, .9, .9)
                    ctx.fill_preserve()
                    ctx.set_source_rgb(0.6, 0.6, 0.6)
                    ctx.set_line_width(self.scale*2)
                    ctx.stroke()
                else:
                    ctx.set_source_rgb(0.6, 0.6, 0.6)
                    ctx.set_line_width(self.scale*2)
                    ctx.stroke()

        return True

    def update(self):
        self.drawingarea.queue_draw()
        if(self.count % self.speed == 0):
            self.game.step()
        self.count += 1
        return True

win = Display()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

