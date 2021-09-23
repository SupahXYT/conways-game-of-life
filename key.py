import gi

def on_release(widget, event):
    print(event.hardware_keycode)


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

win = Gtk.Window()
box = Gtk.EventBox()

win.add_events(Gdk.EventMask.KEY_PRESS_MASK)
win.connect("button-press-event", on_release)
win.connect("key-release-event", on_release)

win.add(box)
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
