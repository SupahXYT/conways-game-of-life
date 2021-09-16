import cairo 
import gi

def draw(da, ctx):
    ctx.rectangle(25, 50, 20, 120)
    ctx.set_source_rgb(1, 0, 0)
    ctx.fill()


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Conway's Game of Life")
window.connect("destroy", Gtk.main_quit)
window.set_default_size(450, 550)

drawingarea = Gtk.DrawingArea()
window.add(drawingarea);
drawingarea.connect('draw', draw)

window.show()
Gtk.main()
