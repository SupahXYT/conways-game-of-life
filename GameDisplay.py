import gi
from random import randrange

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

class frame:

    def __init__(self):
        self.window = Gtk.Window(title="Conway's Game of Life")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_default_size(450, 550)
        self.window.set_border_width(5)

        self.drawingarea = Gtk.DrawingArea()
        self.frame = Gtk.Frame()
        self.frame.set_label("John Conway's Game of Life")
        self.frame.add(self.drawingarea);
        self.window.add(self.frame);
        self.drawingarea.connect('draw', self.draw)
        self.window.show()
        self.frame.show()
        self.drawingarea.show()
        GObject.timeout_add(100, self.refresh) # Go call tick every 50 whatsits.

    def draw(self, da, ctx):
        ctx.set_source_rgb(1, 0, 0)
        ctx.rectangle(randrange(1, 400), 50, 20, 120)
        ctx.fill()
        return True

    def refresh(self):
        self.drawingarea.queue_draw()
        return True

    def main(self):
        Gtk.main()

b = frame()
b.main()

